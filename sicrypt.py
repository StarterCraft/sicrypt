import sys, os, pyperclip, glob, json
import traceback, importlib, requests
import nltk

from PyQt5               import QtCore, QtGui, QtWidgets
from PyQt5.QtCore        import *
from PyQt5.QtGui         import *
from PyQt5.QtWidgets     import *
from uibld               import *
from uibld.settings      import *
from uibld.style         import *


#Global variables declaration
gitHubLink = 'https://github.com/StarterCraft/sicrypt'


class Window(QMainWindow):
    '''
    Main window class
    '''
    #Translate function to simplify translation
    translate = QApplication.translate

    def __init__(self, UIClass: (Ui_MainWindowVertical, Ui_MainWindowHorizontal)):
        QMainWindow.__init__(self)
        self.ui = UIClass()
        self.ui.setupUi(self)

        #Menu for opening a file with specific encoding:
        self.openFileMenu = QMenu()

        #Define and setup encoding actions
        self.openFileEncodingActions = [
            Action('ASCII'),
            Action('ANSI'),
            Action('UTF-8'),
            Action('UTF-16'),
            Action('UTF-32'),
            Action('Windows-1251')]

        self.openFileMenu.addActions(self.openFileEncodingActions)

        #Menu for saving into a file with specific encoding:
        self.saveToFileMenu = QMenu()

        #Define and setup encoding actions
        self.saveToFileEncodingActions = [
            Action('ASCII'),
            Action('ANSI'),
            Action('UTF-8'),
            Action('UTF-16'),
            Action('UTF-32'),
            Action('Windows-1251')]
        self.saveToFileMenu.addActions(self.saveToFileEncodingActions)

        #Bind menus to toolButtons
        self.ui.tbt_OpenFile.setMenu(self.openFileMenu)
        self.ui.tbt_SaveToFile.setMenu(self.saveToFileMenu)


class PlainTextEdit(QPlainTextEdit):
    '''
    An extension to the standard QPlainTextEdit which has an
    overriden 'keyPressEvent' method, allowing to replace Tab
    symbols with spaces, if enabled in the config
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setTabPolicy(self, policy: int) -> None:
        '''
        Set the text field's tab policy. Auxilary method.

        :param 'policy': int
            Policy code, according to which we insert:
            0           —— tab symbol;
            {any+1 > 0} —— corresponding spaces number.
        
        :returns: None    
        '''
        self.tabPolicy = policy


    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Tab:
            QPlainTextEdit.keyPressEvent(self, QKeyEvent(
                QEvent.KeyPress, Qt.Key_Space,
                Qt.KeyboardModifiers(event.nativeModifiers()), ' ' * (self.tabPolicy + 1)) if self.tabPolicy else event)
        else: QPlainTextEdit.keyPressEvent(self, event)


class Action(QAction):
    '''
    A class defenition allowing 'QAction' initialization with
    'data' parameter
    '''
    def __init__(self, name: str, data = None, *args, **kwargs):
        '''
        Initialize QAction with a possibility to set action
        data while initializing

        :kwparam 'data': Any = None
            Optional data
        '''
        QAction.__init__(self, *args, **kwargs)
        self.setText(name)
        if data: self.setData(data)


class Item(QStandardItem):
    '''
    A class defenition allowing 'QStandardItem' initialization with
    'data' parameter.
    '''
    def __init__(self, data = None, *args, **kwargs):
        '''
        Initialize QStandardItem with a possibility to set item
        data while initializing

        :kwparam 'data': Any = None
            Optional data
        '''
        QStandardItem.__init__(self, *args, **kwargs)
        if data: self.setData(data)


class Settings(QDialog):
    '''
    Settings dialog class
    '''
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.loadConfig(noFile = True)

        #Setup UI elements according to current configuration 
        
        #No implementation of language changing yet

        #Ciphers' downloading configuration
        config = self.config['encryption']
        self.ui.ckb_CiphersAllowDownloadingNew.setChecked(config['dlnew'])
        self.ui.ckb_CiphersAllowDownloadingUpdates.setChecked(config['dlupd'])

        #Text fields configuration
        config = self.config['textFields']

        #False for default vertical position,
        #True for horizontal position
        if config['position'] == False: self.ui.rbt_TextFieldsPositionVertical.setChecked(True)
        else: self.ui.rbt_TextFieldsPositionHorizontal.setChecked(True)

        #Setting font
        self.ui.cbb_SourceTextFont.setCurrentFont(QFont(config['font'][0][config['font'][0].index('"'):]))
        self.ui.cbb_SourceTextFont.setCurrentFont(QFont(config['font'][1][config['font'][0].index('"'):]))

        #Setting line wrap
        self.ui.ckb_SourceTextFieldTextWrap.setChecked(config['wrap'][0])
        self.ui.ckb_SourceTextFieldTextWrap.setChecked(config['wrap'][1])

        #Setting tabs policy
        self.ui.cbb_SourceTextFieldTabPolicy.setCurrentIndex(config['tabs'][0])
        self.ui.cbb_SourceTextFieldTabPolicy.setCurrentIndex(config['tabs'][0])


    def loadConfig(self, noFile: bool = False) -> None:
        '''
        Load program configuration from 'config.json' file and save it
        to the 'config' dict. If no config file is initialized, create
        it and write the default config into it.

        :param 'noFile': bool
            If True and no config file is initialized, it will not be
            created.

        :returns: None
        '''
        self.config = {}

        try:
            with open('config.json', 'x') as configFile:
                if noFile: 
                    self.config.update(
                    {'lang': 'en-US',
                    'encryption': {
                        'dlnew': True,
                        'dlupd': True
                    },
                    'textFields': {
                        'position': False,
                        'font': ['13pt "Segoe UI Semilight"', '13pt "Segoe UI Semilight"'],
                        'wrap': [False, False],
                        'tabs': [0, 0]
                    }
                    })
                    return

                else:
                    self.config.update(
                        {'lang': 'en-US',
                         'encryption': {
                            'dlnew': True,
                            'dlupd': True
                           },

                        'textFields': {
                            'position': False,
                            'font': ['13pt "Segoe UI Semilight"', '13pt "Segoe UI Semilight"'],
                            'wrap': [False, False],
                            'tabs': [0, 0]
                            }
                        })

                    json.dump(self.config, configFile)

        except FileExistsError:
            try:
                with open('config.json', 'r') as configFile:
                    self.config.update(json.load(configFile))

            except:
                with open('config.json', 'w') as configFile:
                    self.config.update(
                    {'lang': 'en-US',
                    'encryption': {
                        'dlnew': True,
                        'dlupd': True
                    },
                    'textFields': {
                        'position': False,
                        'font': ['13pt "Segoe UI Semilight"', '13pt "Segoe UI Semilight"'],
                        'wrap': [False, False],
                        'tabs': [0, 0]
                    }
                    })
                    json.dump(self.config, configFile)


    def applyConfig(self, root: Window, onInit: bool = False) -> None:
        '''
        Apply current program configuration from the 'config' dict to the UI.

        :param 'root': Window
            Main window

        :kwparam 'onInit': bool = False
            If true, no MessageBoxes will be generated during the execution
            of the method.

        :returns: None
        '''
        
        #No implementation of language changing yet
        
        #Text fields configuration
        config = self.config['textFields']

        #False for default vertical position,
        #True for horizontal position
        if (type(self.ui) == Ui_MainWindowHorizontal) != self.config['textFields']['position'] and not onInit:
            messageBox(root, QMessageBox.Information, 
                root.translate('TextFieldsPositionChangedDialog', 'Text fields` position has been changed'),
                root.translate('TextFieldsPositionChangedDialog', 'Text fields` position has been changed, changes`ll be applied after restart'))

        #Setting font
        root.ui.ptx_SourceText.setStyleSheet(f'font: {config["font"][0]}')
        root.ui.ptx_ResultText.setStyleSheet(f'font: {config["font"][1]}')

        #Setting line wrap
        root.ui.ptx_SourceText.setLineWrapMode(QPlainTextEdit.WidgetWidth if config['wrap'][0] else QPlainTextEdit.NoWrap)
        root.ui.ptx_ResultText.setLineWrapMode(QPlainTextEdit.WidgetWidth if config['wrap'][1] else QPlainTextEdit.NoWrap)

        #Setting tabs policy
        root.ui.ptx_SourceText.setTabPolicy(config['tabs'][0])
        root.ui.ptx_ResultText.setTabPolicy(config['tabs'][1])


    def handleDialogAcception(self, root: Window) -> None:
        '''
        Read config options selected by user from the UI and make changes
        to 'config' dict, save it into 'config.json' file, then call
        'applyConfig' method to apply the new configuration.

        :returns: None
        '''
        #No implementation of language changing yet
        
        #Ciphers' downloading configuration
        config = self.config['encryption']
        config['dlnew'] = self.ui.ckb_CiphersAllowDownloadingNew.isChecked()
        config['dlupd'] = self.ui.ckb_CiphersAllowDownloadingUpdates.isChecked()

        #Text fields configuration
        config = self.config['textFields']

        #False for default vertical position,
        #True for horizontal position
        config['position'] = self.ui.rbt_TextFieldsPositionHorizontal.isChecked()
        
        #Setting font
        fontFamily = self.ui.cbb_SourceTextFont.currentFont().toString().split(',')[0]
        fontSize   = self.ui.spb_SourceTextFontSize.value()
        config['font'][0] = f'{fontSize}pt "{fontFamily}"'

        fontFamily = self.ui.cbb_ResultTextFont.currentFont().toString().split(',')[0]
        fontSize   = self.ui.spb_ResultTextFontSize.value()
        config['font'][1] = f'{fontSize}pt "{fontFamily}"'

        #Setting line wrap
        config['wrap'][0] = self.ui.ckb_SourceTextFieldTextWrap.isChecked()
        config['wrap'][1] = self.ui.ckb_ResultTextFieldTextWrap.isChecked()

        #Setting tabs policy
        config['tabs'][0] = self.ui.cbb_SourceTextFieldTabPolicy.currentIndex()
        config['tabs'][1] = self.ui.cbb_ResultTextFieldTabPolicy.currentIndex()

        self.config['textFields'].update(config)
        with open('config.json', 'w') as configFile: json.dump(self.config, configFile, indent = 4)

        self.applyConfig(root)


class Cipher:
    '''
    A representation of a cipher, allowing to add custom ciphers to the
    program.

    Ciphers can be one-way (encrypting only, like SHA hashes), or two-way
    (encrypting and decrypting) type.

    You can create your custom cipher(-s) by creating a Python file in
    the 'ciphers' directory and defining class(-es) which inherit the
    'Cipher' class. In your child class you must define two specific
    methods:
        encrypt(self, str) -> str —— the encryption method;
        decrypt(self, str) -> str —— the decryption method.

    As an example, you can refer to the standard 'base64.py' inplemen-
    tation.

    :attrib 'categories': dict<str, Action>
        List of ciphers categories you can pick while initializing a Cipher
        instance
    '''
    categories = {'hash': Action(QApplication.translate('CipherCategories', 'Hashing algorithms')),
                  'simple': Action(QApplication.translate('CipherCategories', 'Simple cryptography')),
                  'btte': Action(QApplication.translate('CipherCategories', 'Binary-to-text encoding'))}



    def __init__(self, type: bool, displayName: str,
        category: str in categories.keys() = '', version: tuple = (1, 0)):
        '''
        Initialize a cipher instance with the following parameters:

        :param 'type': bool
            If True, the cipher expects to have both 'encrypt' and
            'decrypt" methods, so it is a two-way one; if False,
            the cipher expects to have 'encrypt' method only.

        :param 'displayName': str
            The cipher's name that is going to be shown in the ciphers'
            selection combo box.

        :kwparam 'category': str
            Name of the category the cipher belongs to. For example,
            there are hashes, simple cryptography methods like magic
            square, etc. Available categories are:
                'hash'   —— Hashing algorithms;
                'simple' —— Simple cryptography;
                'btte'   —— Binary-to-text encoding.
            By default, the cipher has no category, since categorization
            feature is not yet implemented.

        :kwparam 'version': tuple<int, int>
            Version of the cipher
        '''
        self.type = type
        self.displayName = displayName
        self.category = category
        self.version = version


#Major functions are defined below
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
    global ciphers

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
        for file in requests.get('https://api.github.com/repos/StarterCraft/sicrypt/git/trees/master?recursive=1').json()['tree']:
            try:
                if (file['path'][:file['path'].index('/')] == 'ciphers' and file['path'].endswith('.py')):
                    availableOnGitHub.append(file['path'])
            except ValueError: continue

        for file in availableOnGitHub:
            if file not in available[:]:
                with open(file, 'x') as cipherFile:
                    cipherFile.write(requests.get(f'https://raw.githubusercontent.com/StarterCraft/sicrypt/master/{file}').text)
                available.append(file)

    for fileName in available:
        if fileName.split('/')[len(fileName.split('/'))-1].startswith('__'): continue
        with open(fileName, 'r') as file:
            for line in file.readlines():
                if line.startswith('class '):
                    className = line[5:line.index('(')].strip()
                    if fileName not in classNames.keys():
                        classNames.update({fileName.replace('/', '.'): [className]})
                    else:
                        savedNames = classNames[fileName.replace('/', '.')]
                        savedNames.append(className)
                        classNames.update({fileName.replace('/', '.'): savedNames})

    for classFile, classNames in classNames.items():
        for className in classNames:
            _class = getattr(importlib.import_module(classFile[:-3]), className)
            try:
                if (callable(getattr(_class, 'encrypt')) and
                    callable(getattr(_class, 'decrypt'))):

                    if allowDownloadingUpdates:
                        #Check cipher version via GitHub:
                        #If the cipher is not hosted on GitHub — skip it;
                        #If the cipher is hosted on GitHub and the version there is the same — skip it;
                        #If the cipher is hosted on GitHub and the version there is newer — update it!
                        with open('ciphers/dl.cache', 'w') as file:
                            response = requests.get(f'https://raw.githubusercontent.com/StarterCraft/sicrypt/master/{classFile.replace(".", "/")}')
                            if response == 200: 
                                file.write(response.text)
                                _compareClass = getattr(importlib.import_module('ciphers.dl'), className)
                                if _compareClass.version == _class.version: pass
                                elif _compareClass.version[0] > _class.version[0] or _compareClass.version[1] > _class.version[1]:
                                    with open(classFile, 'w') as originalFile: originalFile.write(response.text)
                                    ciphers.append(_compareClass())

                    ciphers.append(_class())
                    os.system('del ciphers\\dl.cache')

                else: messageBox(root, QMessageBox.Critical,
                    root.translate('CipherLoadingErrorMessagebox', f'Failed to load cipher {className}'),
                    root.translate('CipherLoadingErrorMessagebox', f'Cipher {className}, declared in {classFile}, appears to be invalid'))

            except Exception as exception:
                messageBox(root, QMessageBox.Critical, root.translate('CipherLoadingErrorMessagebox', f'Failed to load cipher {className}'),
                    root.translate('CipherLoadingErrorMessagebox',
                        f'Cipher {className}, declared in {classFile}, failed to load due to {type(exception).__name__}. See the details below'),
                        detalis = f'Our GitHub:{gitHubLink}\n{traceback.format_exc()}')

    for cipher in ciphers: root.ui.cbb_Cipher.addItem(cipher.displayName)
        
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


def encrypt(root: Window) -> None:
    '''
    Encrypt contents of 'Source text' field, and place the encrypted
    text into the 'Result text' field.
        
    :param 'root': Window
        Main window

    :returns: None
    '''
    try:
        root.ui.ptx_ResultText.setPlainText(str(
            getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).encrypt(root.ui.ptx_SourceText.toPlainText())))

    except Exception as exception:
        messageBox(root, QMessageBox.Critical,
            root.translate('EncryptionErrorDialog', 'Failed to encrypt'),
            root.translate('EncryptionErrorDialog', 'Failed to encrypt your text due to an unexpected error.'),
            details = f'Our GitHub: {gitHubLink}\n\n{traceback.format_exc()}')

        
def decrypt(root: Window) -> None:
    '''
    Decrypt contents of 'Source text' field, and place the decrypted
    text into the 'Result text' field.
        
    :param 'root': Window
        Main window

    :returns: None
    '''
    try:
        root.ui.ptx_ResultText.setPlainText(str(
            getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).decrypt(root.ui.ptx_SourceText.toPlainText())))

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
    root.ui.plainTextEdit.setPlainText(str(pyperclip.paste()))


def info(root: Window) -> None:
    '''
    Show 'About' information window.

    :param 'root': Window
        Main window

    :returns: None
    '''
    with open('changelog.txt', 'r') as file: changelog = file.read()
    messageBox(root, QMessageBox.Information, root.translate('AboutDialog', 'About'), 
        root.translate('AboutDialog', 'Developed by: StarterCraft\nVersion: 1.1\n2020-2021'),
        details = changelog)


def openFileDialog(root: Window, encoding: str, flag: bool) -> None:
    '''
    Open file selection dialog for opening a file or saving into a file.

    :param 'root': Window
        Main window

    :param 'encoding': str
        Encoding to open/save a file with. This parameter is transferred
        to the 'openFile'/'saveToFile' methods respectively.

    :param 'flag': bool
        If True, then 'openFile' method will be called after an existing
        file is selected by the user;
        if False, then 'saveToFile' method will be called after any file,
        including a nonexistent one, is selected by the user.

    :returns: None
    '''
    dlg = QFileDialog(root)
    dlg.setOptions(QFileDialog.DontUseNativeDialog)
    dlg.setStyleSheet(styleSheet)
    if flag: dlg.setFileMode(QFileDialog.ExistingFile)
    else: dlg.setFileMode(QFileDialog.AnyFile)
    dlg.show()

    if flag: dlg.fileSelected.connect( lambda: openFile(root, dlg.selectedFiles()[0], encoding) )
    else: dlg.fileSelected.connect( lambda: saveToFile(root, dlg.selectedFiles()[0], encoding) )


def openFile(root: Window, name: str, encoding: str) -> None:
    '''
    Open existing file with specified name and encoding, and place
    the loaded text into the 'Source text' field.
        
    :param 'root': Window
        Main window

    :param 'name': str
        A name of an existing file to open

    :param 'encoding': str
        An encoding to open the file with

    :returns: None
    '''
    try:
        with open(name, 'r', encoding = encoding) as file: root.ui.ptx_SourceText.setPlainText(file.read())
    except Exception as exception:
        messageBox(root, QMessageBox.Critical,
            root.translate('FileOpeningErrorMessagebox', 'An error ocurred while opening file'),
            root.translate('FileOpeningErrorMessagebox', f'Failed to open file "{name}" due to {type(exception).__name__}.'),
            details = f'Our GitHub:{gitHubLink}\n\n{traceback.format_exc()}')


def saveToFile(root: Window, name: str, encoding: str) -> None:
    '''
    Take the text from the 'Resut text' field and save it into a file
    with specified name and encoding.
        
    :param 'root': Window
        Main window

    :param 'name': str
        Any name fo save to the file with

    :param 'encoding': str
        An encoding to save to the file with

    :returns: None
    '''
    try:
        with open(name, 'x', encoding = encoding) as file: file.write(root.ui.ptx_ResultText.toPlainText())
    except FileExistsError:
        if messageBox(root, QMessageBox.Warning,
            root.translate('SavingToFileRewriteMessagebox', 'File you specified already exists'),
            root.translate('SavingToFileRewriteMessagebox', f'File {name} already exists. Should we rewrite it?'),
            buttons = [QMessageBox.Yes, QMessageBox.No]):
            with open(name, 'w', encoding = encoding) as file: file.write(root.ui.ptx_ResultText.toPlainText())
        else: return
    except Exception as exception:
        messageBox(root, QMessageBox.Critical,
            root.translate('SavingToFileErrorMessagebox', 'An error ocurred while saving to file'),
            root.translate('SavingToFileErrorMessagebox', f'Failed to save to file "{name}" due to {type(exception).__name__}.'),
            detais = f'Our GitHub:{gitHubLink}\n\n{traceback.format_exc()}')


def messageBox(root: Window, icon: QMessageBox.Icon, title: str, text: str,
    details: str = None, buttons: list = [QMessageBox.Close]) -> int:
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(appStyleSheet)

    translator = QTranslator(app)
    translator.load(f'qtbase_{QtCore.QLocale.system().name()}', QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    settings = Settings()   
    root = Window(Ui_MainWindowHorizontal if settings.config['textFields']['position'] else Ui_MainWindowVertical)
    settings.applyConfig(root, onInit = True)

    try:
        #Load ciphers
        loadCiphers(root, settings.config['encryption']['dlnew'], settings.config['encryption']['dlupd'])

        #Bind functions to actions and buttons
        root.ui.btn_Encrypt.clicked.connect( lambda: encrypt(root) )
        root.ui.btn_Decrypt.clicked.connect( lambda: decrypt(root) )
        root.ui.btn_Paste.clicked.connect( lambda: pasteSourceText(root) )
        root.ui.btn_Copy.clicked.connect( lambda: copyResultText(root) )
        root.ui.btn_TransferResToSrc.clicked.connect( lambda: transferText(root, True) )
        root.ui.btn_TransferSrcToRes.clicked.connect( lambda: transferText(root, False) ) 
        root.ui.btn_About.clicked.connect( lambda: info(root) )
        root.ui.btn_Settings.clicked.connect( settings.open )
        root.ui.tbt_OpenFile.clicked.connect( lambda: openFileDialog(root, 'utf-8', True) )
        root.ui.cbb_Cipher.currentTextChanged.connect( 
           lambda: (root.ui.btn_Decrypt.setEnabled(False) if not getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).type
               else root.ui.btn_Decrypt.setEnabled(True)) )
        for action in root.openFileEncodingActions: action.triggered.connect( lambda: openFileDialog(root, action.text().lower(), True) )
        for action in root.saveToFileEncodingActions: action.triggered.connect( lambda: openFileDialog(root, action.text().lower(), False) )

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
