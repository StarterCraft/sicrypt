import sys, os, pyperclip, glob, json
import traceback, importlib, requests, subprocess

from PySide6             import QtCore, QtGui, QtWidgets
from uibld               import *
from uibld.settings      import *
from uibld.style         import *


#Global variables declaration
gitHubLink = 'https://github.com/StarterCraft/sicrypt'
version = 'v1.3'


class Sicrypt(QtWidgets.QApplication):
    #Major functions are defined below
    def initUi(root: Window, settings: Settings):
        root.ui.cbb_Cipher.setToolTip(ciphers[0].getInformation(root))

        checkForUpdates(root)

        #Bind functions to actions and buttons
        root.ui.tbt_Encrypt.clicked.connect( lambda: encrypt(root, 'utf-8') )
        root.ui.tbt_Decrypt.clicked.connect( lambda: decrypt(root, 'utf-8') )
        root.ui.btn_Paste.clicked.connect( lambda: pasteSourceText(root) )
        root.ui.btn_Copy.clicked.connect( lambda: copyResultText(root) )
        root.ui.btn_TransferResToSrc.clicked.connect( lambda: transferText(root, True) )
        root.ui.btn_TransferSrcToRes.clicked.connect( lambda: transferText(root, False) ) 
        root.ui.btn_About.clicked.connect( lambda: info(root) )
        root.ui.btn_Settings.clicked.connect( settings.open )
        root.ui.tbt_OpenFile.clicked.connect( lambda: openFileDialog(root, 'utf-8', True, root.openFileActionGroup.actions()[0].isChecked()) )
        root.ui.tbt_SaveToFile.clicked.connect( lambda: openFileDialog(root, 'utf-8', False, root.saveToFileActionGroup.actions()[0].isChecked()) )
        root.ui.cbb_Cipher.currentTextChanged.connect( lambda: switchCurrentCipher(root) )

        for action in root.openFileActionGroup.actions(): 
            if action.text()[1:7] == 'Source': action.setChecked(True)

        for action in root.saveToFileActionGroup.actions(): 
            if action.text()[1:7] == 'Result': action.setChecked(True)

        for i in range(0, 4):
            for action in root.encodingActions[i]:
                if i in range(0, 2): action.triggered.connect( lambda: openFileDialog(root, action.text().lower(), action.data()) )
                elif i == 2: action.triggered.connect( lambda: encrypt(root, action.text().lower()) )
                elif i == 3: action.triggered.connect( lambda: decrypt(root, action.text().lower()) )

        for customEncodingAction in root.customEncodingActions: customEncodingAction.triggered.connect( 
            lambda: (openFileDialog(root,
                inputDialog(root, root.tr('Custom encoding'), root.tr('Specify an encoding...')).lower(), customEncodingAction.data()) 
                if customEncodingAction.data() in range(0, 2) else (customEncodingAction.triggered.connect(
                    lambda: encrypt(root, inputDialog(root, root.tr('Custom encoding'), root.tr('Specify an encoding...')).lower())
                    if action.data() == 2 else customEncodingAction.triggered.connect(
                        lambda: decrypt(root, inputDialog(root, root.tr('Custom encoding'), root.tr('Specify an encoding...')).lower())
                )))))
            
        addCiphersToCbbCipher(root)


    def checkForUpdates(root: Window):
        '''
        Check for updates, and if there is one, ask the user
        if he wants to update the program.

        :param 'root': Window
            Main window

        :returns: None
        '''
        try:
            response = getRequest(root, 'https://api.github.com/repos/StarterCraft/sicrypt/releases/latest').json()
            tag = response['tag_name']
            if int(tag[1:2]) > int(version[1:2]) or int(tag[3:4]) > int(version[3:4]):
                if messageBox(root, QMessageBox.Information,
                    root.translate('UpdateDialog', 'Update available'),
                    root.translate('UpdateDialog', f'Update {tag} is available, would you like to download and install it?'),
                    details = getRequest(root, 'https://raw.githubusercontent.com/StarterCraft/sicrypt/master/changelog.txt').text,
                    buttons = [QMessageBox.Yes, QMessageBox.No]):
                    installerURL = getRequest(root, response['assets_url']).json()['browser_download_url']

                    with requests.get(installerURL, stream = True) as request:
                        request.raise_for_status()
                        with open('installer.exe', 'wb') as f:
                            for chunk in request.iter_content(chunk_size = None):
                                if chunk: f.write(chunk)

                    subprocess.Popen('installer.exe', creationflags = subprocess.CREATE_NEW_CONSOLE)
                    exit(1)
                else: return
        except KeyError: #github api does not return a valid message
            pass


    def loadCiphers(root: Window, allowDownloadingNew: bool, allowDownloadingUpdates: bool) -> None:
        '''
        Load ciphers from '*.py' files in 'ciphers' directory,
        initialize them, collect them into 'ciphers' list and
        add their display names to the cipher selection combobox.

        :param 'root': Window
            Main window

        :param 'allowDownloadingNew': bool
            Allow downloading new (uninstalled locally) ciphers from our GitHub

        :param 'allowDownloadingUpdates': bool
            Allow downloading updated ciphers from our GitHub

        :returns: None
        '''
        global ciphers, categories

        ciphers, categories, classNames = [], [], {}
        available = glob.glob('ciphers/*')
        if not available:
            try: os.mkdir('ciphers')
            except FileExistsError: pass

        for fileName in available[:]:
            available.remove(fileName)
            available.append(fileName.replace('\\', '/'))

        #Find now ciphers on GitHub
        if allowDownloadingNew:
            availableOnGitHub = []

            try:
                for file in getRequest(root, 'https://api.github.com/repos/StarterCraft/sicrypt/git/trees/master?recursive=1').json()['tree']:
                    try:
                        if (file['path'][:file['path'].index('/')] == 'ciphers' and file['path'].endswith('.py')):
                            availableOnGitHub.append(file['path'])
                    except ValueError: continue
            except KeyError:
                pass

            for file in availableOnGitHub:
                if file not in available[:]:
                    with open(file, 'x') as cipherFile:
                        cipherFile.write(getRequest(root, f'https://raw.githubusercontent.com/StarterCraft/sicrypt/master/{file}').text)
                    available.append(file)

        for fileName in available:
            if fileName.split('/')[len(fileName.split('/'))-1].startswith('__'): continue
            with open(fileName, 'r', encoding = 'utf-8') as file:
                for line in file.readlines():
                    if line.startswith('class '):
                        className = line[5:line.index('(')].strip()
                        if fileName.replace('/', '.') not in classNames.keys():
                            classNames.update({fileName.replace('/', '.'): [className]})
                        else:
                            savedNames = classNames[fileName.replace('/', '.')]
                            savedNames.append(className)
                            classNames.update({fileName.replace('/', '.'): savedNames})

        loading = QProgressDialog('Downloading ciphers...', 'Abort', 0, len(classNames.items()))
        loading.setWindowTitle('Downloading ciphers...')
        loading.setWindowModality(Qt.WindowModality.WindowModal)
        loading.setValue(0)
        loading.show()
        cix = 0

        for classFile, classNames in classNames.items():
            loading.setValue(cix)

            for className in classNames:
                _class = getattr(importlib.import_module(classFile[:-3]), className)
                try:
                    if (callable(getattr(_class, 'encrypt')) and
                    (callable(getattr(_class, 'decrypt')) if getattr(_class(), 'type') else True)):

                        if allowDownloadingUpdates:
                            #Check cipher version via GitHub:
                            #If the cipher is not hosted on GitHub — skip it;
                            #If the cipher is hosted on GitHub and the version there is the same — skip it;
                            #If the cipher is hosted on GitHub and the version there is newer — update it!
                            with open('ciphers/dl.cache', 'w', encoding = 'utf-8') as file:
                                response = getRequest(root, f'https://raw.githubusercontent.com/StarterCraft/sicrypt/master/{classFile.replace(".", "/")}')
                                if response == 200: 
                                    file.write(response.text)
                        
                                    _compareClass = getattr(importlib.import_module('ciphers.dl'), className)
                                    if _compareClass.version == _class.version: pass
                                    elif _compareClass.version[0] > _class.version[0] or _compareClass.version[1] > _class.version[1]:
                                        with open(classFile, 'w') as originalFile: originalFile.write(response.text)
                                        ciphers.append(_compareClass())

                        ciphers.append(_class())
                        os.remove('ciphers/dl.cache')

                    else: messageBox(root, QMessageBox.Critical,
                        root.translate('CipherLoadingErrorMessagebox', f'Failed to load cipher {className}'),
                        root.translate('CipherLoadingErrorMessagebox', f'Cipher {className}, declared in {classFile}, appears to be invalid'))

                except Exception as exception:
                    messageBox(root, QMessageBox.Critical, root.translate('CipherLoadingErrorMessagebox', f'Failed to load cipher {className}'),
                        root.translate('CipherLoadingErrorMessagebox',
                            f'Cipher {className}, declared in {classFile}, failed to load due to {type(exception).__name__}. See the details below'),
                            details = f'Our GitHub: {gitHubLink}\n{traceback.format_exc()}')
                    
            cix += 1

            if (loading.wasCanceled()): 
                return
            
        loading.hide()


    def addCiphersToCbbCipher(root: Window):
        for cipher in ciphers:
            if cipher.category not in categories: categories.append(cipher.category)

        for category in categories:
            i = 0

            for cipher in ciphers: 
                if cipher.category == category: root.ui.cbb_Cipher.addItem(cipher.displayName)
                i += 1

            if len(categories) > 1: root.ui.cbb_Cipher.insertSeparator(i)
            
        #TODO No.1: Implement QComboBox with categories 
        #Setup model for the cipher selection combobox
        #cipherSelectionModel = QStringListModel()

        #(https://stackoverflow.com/questions/33012292/grouped-qcombobox)
        #cipherSelectionModel.setStringList([cipher.displayName for cipher in ciphers])


    def getCipherByDisplayName(name: str) -> Cipher:
        '''
        Find the 'Cipher' class instance in the 'ciphers' list, which
        display name maches the 'name' parameter, and return it. This
        method is used while a cipher is selected in the cipher sele-
        ction combobox.

        :param 'name': str
            Display name for finding the 'Cipher' class instance

        :returns: Cipher
        '''
        for cipher in ciphers:
            if cipher.displayName == name: return cipher


    def switchCurrentCipher(root: Window) -> None:
        '''
        Switch the current selected cipher.
            
        :param 'root': Window
            Main window

        :returns: None
        '''
        root.ui.tbt_Decrypt.setEnabled(False) if not getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).type else root.ui.tbt_Decrypt.setEnabled(True)
        root.ui.cbb_Cipher.setToolTip(root.tr('Select your cipher\n\nSelected cipher`s propreties:\n') + 
                                    getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).getInformation(root))


    def encrypt(root: Window, encoding: str) -> None:
        '''
        Encrypt contents of 'Source text' field, and place the encrypted
        text into the 'Result text' field.
            
        :param 'root': Window
            Main window

        :param 'encoding': str
            Encoding to encrypt the text with

        :returns: None
        '''
        try:
            root.ui.ptx_ResultText.setPlainText(str(
                getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).encrypt(root.ui.ptx_SourceText.toPlainText(), encoding)))

        except Exception as exception:
            messageBox(root, QMessageBox.Critical,
                root.translate('EncryptionErrorDialog', 'Failed to encrypt'),
                root.translate('EncryptionErrorDialog', 'Failed to encrypt your text due to an unexpected error.'),
                details = f'Our GitHub: {gitHubLink}\n\n{traceback.format_exc()}')

            
    def decrypt(root: Window, encoding: str) -> None:
        '''
        Decrypt contents of 'Source text' field, and place the decrypted
        text into the 'Result text' field.
            
        :param 'root': Window
            Main window

        :param 'encoding': str
            Encoding to decrypt the text with

        :returns: None
        '''
        try:
            root.ui.ptx_ResultText.setPlainText(str(
                getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).decrypt(root.ui.ptx_SourceText.toPlainText(), encoding)))

        except AttributeError:
            messageBox(root, QMessageBox.Critical,
                root.translate('DecryptionErrorDialog', 'Failed to decrypt: this cipher is one-way'),
                root.translate('DecryptionErrorDialog', 'Failed to decrypt your text due to the selected cipher not suppporting decryption.'),
                details = f'Our GitHub: {gitHubLink}\n\n{traceback.format_exc()}')

        except Exception as exception:
            messageBox(root, QMessageBox.Critical,
                root.translate('DecryptionErrorDialog', 'Failed to decrypt'),
                root.translate('DecryptionErrorDialog', 'Failed to decrypt your text due to an unexpected error.'),
                details = f'Our GitHub: {gitHubLink}\n\n{traceback.format_exc()}')


    def transferText(root: Window, flag: bool) -> None:
        '''
        Tranfer text between the two text fields.
            
        :param 'root': Window
            Main window

        :param 'flag': bool
            Mode switch. 
            If True, transfer text from 'Result text' field to 'Source text' field;
            if False, transfer text from 'Source text' field to 'Result text' field

        :returns: None
        '''
        if flag: #Transfer text from 'Result text' field to 'Source text' field
            root.ui.ptx_SourceText.setPlainText(root.ui.ptx_ResultText.toPlainText())
            root.ui.ptx_ResultText.clear()
        else:    #Transfer text from 'Source text' field to 'Result text' field
            root.ui.ptx_ResultText.setPlainText(root.ui.ptx_SourceText.toPlainText())
            root.ui.ptx_SourceText.clear()


    def copyResultText(root: Window) -> None:
        '''
        Copy result text to the clipboard.

        :param 'root': Window
            Main window

        :returns: None
        '''
        pyperclip.copy(root.ui.ptx_ResultText.toPlainText())


    def pasteSourceText(root: Window) -> None:
        '''
        Paste clipboard text as source text.

        :param 'root': Window
            Main window

        :returns: None
        '''
        root.ui.ptx_SourceText.setPlainText(str(pyperclip.paste()))


    def info(root: Window) -> None:
        '''
        Show 'About' information window.

        :param 'root': Window
            Main window

        :returns: None
        '''
        changelog = getRequest(root, 'https://raw.githubusercontent.com/StarterCraft/sicrypt/master/changelog.txt').text
        messageBox(root, QMessageBox.Information, root.translate('AboutDialog', 'About'), 
            root.translate('AboutDialog', f'Developed by: StarterCraft\nVersion: {version}\n2020-2021'),
            details = changelog)


    def openFileDialog(root: Window, encoding: str, flag: int, fieldFlag: bool) -> None:
        '''
        Open file selection dialog for opening a file or saving into a file.

        :param 'root': Window
            Main window

        :param 'encoding': str
            Encoding to open/save a file with. This parameter is transferred
            to the 'openFile'/'saveToFile' methods respectively.

        :param 'flag': int
            If 0, then 'openFile' method will be called after an existing
            file is selected by the user;
            if 1, then 'saveToFile' method will be called after any file,
            including a nonexistent one, is selected by the user.

        :param 'fieldFlag': bool
            Determines which text field is going to be used while working
            with the text; False for 'Source text', True for 'Result text'
            fields.

        :returns: None
        '''
        dlg = QFileDialog(root)
        dlg.setOptions(QFileDialog.DontUseNativeDialog)
        dlg.setStyleSheet(styleSheet)
        if flag: dlg.setFileMode(QFileDialog.ExistingFile)
        else: dlg.setFileMode(QFileDialog.AnyFile)
        dlg.show()

        if flag: dlg.fileSelected.connect( lambda: openFile(root, dlg.selectedFiles()[0], encoding, fieldFlag) )
        else: dlg.fileSelected.connect( lambda: saveToFile(root, dlg.selectedFiles()[0], encoding, fieldFlag) )


    def openFile(root: Window, name: str, encoding: str, fieldFlag: bool) -> None:
        '''
        Open existing file with specified name and encoding, and place
        the loaded text into the 'Source text' field.
            
        :param 'root': Window
            Main window

        :param 'name': str
            A name of an existing file to open

        :param 'encoding': str
            An encoding to open the file with

        :param 'fieldFlag': bool
            Determines which text field is going to be used while working
            with the text; False for 'Source text', True for 'Result text'
            fields.

        :returns: None
        '''
        try:
            with open(name, 'r', encoding = encoding) as file: 
                (root.ui.ptx_SourceText.setPlainText(file.read()) if fieldFlag else root.ui.ptx_ResultText.setPlainText(file.read()))
        except Exception as exception:
            messageBox(root, QMessageBox.Critical,
                root.translate('FileOpeningErrorMessagebox', 'An error ocurred while opening file'),
                root.translate('FileOpeningErrorMessagebox', f'Failed to open file "{name}" due to {type(exception).__name__}.'),
                details = f'Our GitHub:{gitHubLink}\n\n{traceback.format_exc()}')


    def saveToFile(root: Window, name: str, encoding: str, fieldFlag: bool) -> None:
        '''
        Take the text from the 'Resut text' field and save it into a file
        with specified name and encoding.
            
        :param 'root': Window
            Main window

        :param 'name': str
            Any name fo save to the file with

        :param 'encoding': str
            An encoding to save to the file with

        :param 'fieldFlag': bool
            Determines which text field is going to be used while working
            with the text; False for 'Source text', True for 'Result text'
            fields.

        :returns: None
        '''
        try:
            with open(name, 'x', encoding = encoding) as file:
                (file.write(root.ui.ptx_SourceText.toPlainText()) if fieldFlag else file.write(root.ui.ptx_ResultText.toPlainText()))
        except FileExistsError:
            if messageBox(root, QMessageBox.Warning,
                root.translate('SavingToFileRewriteMessagebox', 'File you specified already exists'),
                root.translate('SavingToFileRewriteMessagebox', f'File {name} already exists. Should we rewrite it?'),
                buttons = [QMessageBox.Yes, QMessageBox.No]):
                with open(name, 'w', encoding = encoding) as file: 
                    (file.write(root.ui.ptx_SourceText.toPlainText()) if fieldFlag else file.write(root.ui.ptx_ResultText.toPlainText()))
            else: return

        except Exception as exception:
            messageBox(root, QMessageBox.Critical,
                root.translate('SavingToFileErrorMessagebox', 'An error ocurred while saving to file'),
                root.translate('SavingToFileErrorMessagebox', f'Failed to save to file "{name}" due to {type(exception).__name__}.'),
                details = f'Our GitHub:{gitHubLink}\n\n{traceback.format_exc()}')


    def messageBox(root: Window, icon: QMessageBox.Icon, title: str, text: str,
        details: str = None, buttons: list[QMessageBox.StandardButton] = [QMessageBox.Close]) -> int:
        '''
        Show a messagebox with the given icon, title, and text.
        Buttons of the message box can be modified and detailed
        text can be applied if necessary.
            
        :param 'root': Window
            Main window

        :param 'icon': QMessageBox.Icon
            A standard QMessageBox.Icon to show in the messagebox

        :param 'title': str
            Messagebox's title

        :param 'text': str
            Messagebox's main text

        :kwparam 'details': str = None
            Optional detailed text

        :kwparam 'buttons': list<QMessageBox.StandardButtons> = [QMessageBox.Close]
            Buttons that should be shown in the messageBox,
            defaults to one 'Close' button.

        :returns: int
            The integer value representing the user's response
            to the messagebox, according to Qt5 Messagebox Button
            Roles.
        '''
        _messageBox = QMessageBox(icon, title, text, parent = root)
        if details: _messageBox.setDetailedText(details)

        for buttonDef in buttons:
            btn = _messageBox.addButton(buttonDef)
            btn.setStyleSheet(buttonStyleSheet)

        _messageBox.setStyleSheet(styleSheet)
        _messageBox.layout().setSizeConstraint(QLayout.SetMinimumSize)
        return _messageBox.exec()


    def inputDialog(root: Window, title: str, text: str) -> str:
        '''
        Show an input dialog with the given title and text.
            
        :param 'root': Window
            Main window

        :param 'title': str
            Input dialog's title

        :param 'text': str
            Input dialog's main text

        :returns: str
            String the user entered.
        '''
        _dialog = QInputDialog(root)
        _dialog.setWindowTitle(title)
        _dialog.setLabelText(text)
        _dialog.setStyleSheet(styleSheet)
        _dialog.setOkButtonText(_dialog.tr('Confirm and resume'))
        _dialog.setInputMode(QInputDialog.TextInput)
        _dialog.exec_()
        return _dialog.textValue()


    def getRequest(root: Window, url: str):
        try: return requests.get(url)
        except Exception as exception: messageBox(root, QMessageBox.Critical,
            root.translate('RequestErrorMessagebox', 'Internet connection error'),
            root.translate('RequestErrorMessagebox', f'Failed to make a GET request due to {type(exception).__name__}.'),
            details = f'Our GitHub:{gitHubLink}\n\n{traceback.format_exc()}')


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(appStyleSheet)

    translator = QTranslator(app)
    translator.load(f'qtbase_{QtCore.QLocale.system().name()}', QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    settings = Settings()   
    root = Window(Ui_MainWindowHorizontal if settings.config['textFields']['position'] else Ui_MainWindowVertical, settings)
    settings.applyConfig(root, onInit = True)

    try:
        #Load ciphers
        loadCiphers(root, settings.config['encryption']['dlnew'], settings.config['encryption']['dlupd'])
        
        checkForUpdates(root)

        initUi(root, settings)

        #Settings dialog
        settings.accepted.connect( lambda: settings.handleDialogAcception(root) )

        #Execute the program
        root.show()
        sys.exit(app.exec_())


    except KeyboardInterrupt: exit(1)
    
    except Exception as exception:
        messageBox(root, QMessageBox.Critical,
            root.translate('CriticalErrorDialog', 'An unexpected error forced Sicrypt to close'),
            root.translate('CriticalErrorDialog', 
                f'An critical {type(exception).__name__} occured, see the details below (click "Show details..." button '
                f'to see details). Please submit an issue on our GitHub, so we can help you solving this problem. If you '
                 'have fixed this problem yourself, huge thanks to you, please submit a pull request with the code files '
                 'you have changed.'),
                details = f'Our GitHub: {gitHubLink}\n\n{traceback.format_exc()}')

if __name__ == '__main__':
    main()    
