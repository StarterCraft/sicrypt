import sys, os, pyperclip, glob, json
import importlib, requests

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

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
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

    def loadConfig(self) -> None:
        '''
        Load program configuration from 'config.json' file and apply it
        to the UI.

        :returns: None
        '''
        self.config = {}
        with open('config.json', 'r') as file: self.config.update(json.load(file))


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
    categories = {'hash': Action(Window.translate('CipherCategories', 'Hashing algorithms')),
                  'simple': Action(Window.translate('CipherCategories', 'Simple cryptography')),
                  'btte': Action(Window.translate('CipherCategories', 'Binary-to-text encoding'))}



    def __init__(self, type: bool, displayName: str, category: str in categories.keys()):
        '''
        Initialize a cipher instance with the following parameters:

        :param 'type': bool
            If True, the cipher expects to have both 'encrypt' and
            'decrypt" methods, so it is a two-way one; if False,
            the cipher expects to have 'encrypt' method only.

        :param 'displayName': str
            The cipher's name that is going to be shown in the ciphers'
            selection combo box.

        :param 'category': str
            Name of the category the cipher belongs to. For example,
            there are hashes, simple cryptography methods like magic
            square, etc. Available categories are:
                'hash'   —— Hashing algorithms;
                'simple' —— Simple cryptography;
                'btte'   —— Binary-to-text encoding.
        '''
        self.type = type
        self.displayName = displayName
        self.category = category


#Major functions are defined below
def loadCiphers(root: Window) -> None:
    '''
    Load ciphers from '*.py' files in 'ciphers' directory,
    initialize them, collect them into 'ciphers' list and
    add their display names to the cipher selection combobox.

    :param 'root': Window
        Main window

    :returns: None
    '''
    global ciphers

    ciphers, categories, classNames = [], [], {}
    available = glob.glob('ciphers/*')
    for fileName in available[:]:
        available.remove(fileName)
        available.append(fileName.replace('\\', '/'))

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
            _class = getattr(importlib.import_module(classFile[:-3], 'ciphers'), className)

            try:
                if (callable(getattr(_class, 'encrypt')) and
                    callable(getattr(_class, 'decrypt'))):
                    ciphers.append(_class())
                else: messageBox(root, QMessageBox.Critical,
                    root.translate('CipherLoadingErrorMessagebox', f'Failed to load cipher {className}'),
                    root.translate('CipherLoadingErrorMessagebox', f'Cipher {className}, declared in {classFile}, appears to be invalid'))

            except Exception as exception:
                messageBox(root, QMessageBox.Critical, root.translate('CipherLoadingErrorMessagebox', f'Failed to load cipher {className}'),
                    root.translate('CipherLoadingErrorMessagebox',
                        f'Cipher {className}, declared in {classFile}, failed to load due to {type(exception).__name__}. See the details below'),
                        details = str(exception))

    for cipher in ciphers: 
        if cipher.category not in categories: categories.append(cipher.category)
        root.ui.cbb_Cipher.addItem(cipher.displayName)
        
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
    root.ui.ptx_ResultText.setPlainText(str(
        getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).encrypt(root.ui.ptx_SourceText.toPlainText())))

        
def decrypt(root: Window) -> None:
    '''
    Decrypt contents of 'Source text' field, and place the decrypted
    text into the 'Result text' field.
        
    :param 'root': Window
        Main window

    :returns: None
    '''
    root.ui.ptx_ResultText.setPlainText(str(
        getCipherByDisplayName(root.ui.cbb_Cipher.currentText()).decrypt(root.ui.ptx_SourceText.toPlainText())))


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
        root.translate('AboutDialog', 'Developed by: StarterCraft\n Version: 1.1\n2020-2021'),
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
            root.translate('FileOpeningErrorMessagebox', f'Failed to open file "{name}" due to {type(exception).__name__}',
            details = str(exception)))


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
            root.translate('SavingToFileErrorMessagebox', f'Failed to save to file "{name}" due to {type(exception).__name__}',
            details = str(exception)))


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
    return _messageBox.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(appStyleSheet)

    translator = QTranslator(app)
    translator.load(f'qtbase_{QtCore.QLocale.system().name()}', QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    root = Window()


    try:
        #Load ciphers
        loadCiphers(root)

        #Bind functions to actions
        root.ui.btn_Encrypt.clicked.connect( lambda: encrypt(root) )
        root.ui.btn_Decrypt.clicked.connect( lambda: decrypt(root) )
        root.ui.btn_Paste.clicked.connect( lambda: pasteSourceText(root) )
        root.ui.btn_Copy.clicked.connect( lambda: copyResultText(root) )
        root.ui.btn_TransferResToSrc.clicked.connect( lambda: transferText(root, True) )
        root.ui.btn_TransferSrcToRes.clicked.connect( lambda: transferText(root, False) ) 
        root.ui.btn_About.clicked.connect( lambda: info(root) )
        root.ui.tbt_OpenFile.clicked.connect( lambda: openFileDialog(root, 'utf-8', True) )
        for action in root.openFileEncodingActions: action.triggered.connect( lambda: openFileDialog(root, action.text().lower(), True) )
        for action in root.saveToFileEncodingActions: action.triggered.connect( lambda: openFileDialog(root, action.text().lower(), False) )

        #Execute the program
        root.show()
        sys.exit(app.exec_())


    except KeyboardInterrupt: exit(1)
    
    except Exception as exception:
        messageBox(root, QMessageBox.Critical,
            root.translate('CriticalErrorDialog', 'An unexpected error forced Sicrypt to close'),
            root.translate('CriticalErrorDialog', f'An critical {type(exception).__name__} occured, see the details below '
                f'(click "Show details..." button to see details). Please submit an issue on our GitHub here: {gitHubLink}, ',
                'so we can help you solving this problem. If you have fixed this problem yourself, huge thanks to you, '
                'please submit a pull request with the code files you have changed.'),
            details = str(exception))
