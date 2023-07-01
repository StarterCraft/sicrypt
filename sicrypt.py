import sys, os, pyperclip, glob, json
from PyQt5.QtWidgets import QWidget
import traceback, importlib, requests, subprocess

from PyQt5               import QtCore
from PyQt5.QtCore        import *
from PyQt5.QtGui         import *
from PyQt5.QtWidgets     import *
from typing              import Callable, Iterator, Tuple
from uibld               import *
from uibld.settings      import *
from uibld.style         import *


#Global variables declaration
gitHubLink = 'https://github.com/StarterCraft/sicrypt'
version = 'v1.3'
ciphers = []
categories = []


class Window(QMainWindow):
    '''
    Main window class
    '''
    #Translate function to simplify translation
    translate = QApplication.translate

    def __init__(self, UIClass: Ui_MainWindowVertical | Ui_MainWindowHorizontal, config):
        QMainWindow.__init__(self)
        self.ui = UIClass()
        self.ui.setupUi(self)

        #Menu for encrypting text with specific encoding:
        self.encryptMenu = QMenu()

        #Menu for decrypting text with specific encoding:
        self.decryptMenu = QMenu()

        #Menu for opening a file with specific encoding:
        self.openFileMenu = QMenu()

        #Menu for saving into a file with specific encoding:
        self.saveToFileMenu = QMenu()

        #Add actions to select a text field to get the file's text into
        self.openFileActionGroup = QActionGroup(self)
        self.openFileActionGroup.addAction(Action(self.tr("'Source text' field"), data = False))
        self.openFileActionGroup.addAction(Action(self.tr("'Result text' field"), data = False))
        self.openFileActionGroup.setExclusive(True)

        for action in self.openFileActionGroup.actions():
            action.setCheckable(True)
            self.openFileMenu.addAction(action)

        self.openFileMenu.addSeparator()
            
        #Add actions to select a text field to get the file's text into
        self.saveToFileActionGroup = QActionGroup(self)
        self.saveToFileActionGroup.addAction(Action(self.tr("'Source text' field"), data = True))
        self.saveToFileActionGroup.addAction(Action(self.tr("'Result text' field"), data = True))
        self.saveToFileActionGroup.setExclusive(True)

        for action in self.saveToFileActionGroup.actions():
            action.setCheckable(True)
            self.saveToFileMenu.addAction(action)

        self.saveToFileMenu.addSeparator()

        #Define and setup encoding actions
        self.encodingActions = [] 

        for i in range(0, 4):
            self.encodingActions.append([
                Action('ASCII', data = i),
                Action('ANSI', data = i),
                Action('UTF-8', data = i),
                Action('UTF-16', data = i),
                Action('UTF-32', data = i),
                Action('Windows-1251', data = i)])

        for action in self.encodingActions[2]: self.encryptMenu.addAction(action)
        for action in self.encodingActions[3]: self.decryptMenu.addAction(action)
        for action in self.encodingActions[0]: self.openFileMenu.addAction(action)
        for action in self.encodingActions[1]: self.saveToFileMenu.addAction(action)

        self.customEncodingActions = [Action(self.tr('Other...'), data = i) for i in range(0, 4)]

        self.encryptMenu.addAction(self.customEncodingActions[2])
        self.decryptMenu.addAction(self.customEncodingActions[3])
        self.openFileMenu.addAction(self.customEncodingActions[0])
        self.saveToFileMenu.addAction(self.customEncodingActions[1])

        #Bind menus to toolButtons
        self.ui.tbt_Encrypt.setMenu(self.encryptMenu)
        self.ui.tbt_Decrypt.setMenu(self.decryptMenu)
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
        if event.key() == Qt.Key_Tab and self.tabPolicy:
            QPlainTextEdit.keyPressEvent(self, QKeyEvent(
                QEvent.KeyPress, Qt.Key_Space,
                Qt.KeyboardModifiers(event.nativeModifiers()), ' ' * (self.tabPolicy + 1)))
        else: QPlainTextEdit.keyPressEvent(self, event)


class Action(QAction):
    '''
    A class defenition allowing 'QAction' initialization with
    additional settings, such as setting data, automatically adding
    the action to one menu or multiple ones, or connect 'triggered'
    signal to a method.
    '''
    def __init__(self, name: str, data = None,
                 menu: QMenu = None, menus: list[QMenu] = None,
                 onTriggered: Callable = None,  
                 *args, **kwargs):
        '''
        Initialize QAction with a possibility to set action
        data while initializing

        :kwparam 'data': Any = None
            Optional data

        :kwparam 'menu': QMenu = None
            Optional QMenu to add the action to
        '''
        QAction.__init__(self, *args, **kwargs)
        self.setText(name)
        if data: self.setData(data)
        if menu: menu.addAction(self)
        if onTriggered: self.triggered.connect(onTriggered)


    def modifyData(self, data):
        '''
        Set action data and return the action itself

        :param 'data': Any
            Data

        :returns: Action
        '''
        self.setData(data)
        return self


class Item(QStandardItem):
    '''
    A class defenition allowing 'QStandardItem' initialization with
    additional settings, such as setting data and adding a tooltip
    with the given text.
    '''
    def __init__(self, text: str, data = None, toolTipText: str = None, *args, **kwargs):
        '''
        Initialize QStandardItem with a possibility to set item
        data while initializing

        :kwparam 'data': Any = None
            Optional data
        '''
        QStandardItem.__init__(self, *args, **kwargs)
        if data: self.setData(data)
        if toolTipText: self.setToolTip(toolTipText)


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
                            'open': False,
                            'save': True,
                            'font': ['13pt "Segoe UI Semilight"', '13pt "Segoe UI Semilight"'],
                            'wrap': [False, False],
                            'tabs': [0, 0]
                        }})
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
                            'open': False,
                            'save': True,
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
                            'open': False,
                            'save': True,
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
        if (not onInit):
            print(('Гориз сейчас' if type(root.ui) == Ui_MainWindowHorizontal else'Верт сейчас'), "хочу", ('гориз' if self.config['textFields']['position'] else 'верт'))
            if (type(root.ui) == Ui_MainWindowHorizontal) != self.config['textFields']['position']:
                root.ui = (Ui_MainWindowHorizontal if self.config['textFields']['position'] else Ui_MainWindowVertical)()
                root.ui.setupUi(root)
                initUi(root, self)

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


class CipherLoadingDialog(QDialog):
    def __init__(self):
        QDialog.__init__()

        self.setStyleSheet(styleSheet)

        self.label = QLabel(self.tr('Загрузка шифров... Пожалуйста, подождите.'))
        self.pgbar = QProgressBar()

        self.show()


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
        encrypt(self, str, encoding) -> str —— the encryption method;
        decrypt(self, str, encoding) -> str —— the decryption method.

    By default, UTF-8 encoding is used.

    As an example, you can refer to the standard 'base64.py' inplemen-
    tation.

    :attrib 'categories': dict<str, Action>
        List of ciphers categories you can pick while initializing a Cipher
        instance
    '''
    categories = {'hash': Action(QApplication.translate('CipherCategories', 'Hashing algorithm')),
                  'simple': Action(QApplication.translate('CipherCategories', 'Simple cryptography')),
                  'btte': Action(QApplication.translate('CipherCategories', 'Binary-to-text encoding'))}


    def __init__(self, type: bool, displayName: str, origin: str,
        category: str in categories.keys(), version: tuple[int] = (1, 0)):
        '''
        Initialize a cipher instance with the following parameters:

        :param 'type': bool
            If True, the cipher expects to have both 'encrypt' and
            'decrypt" methods, so it is a two-way one; if False,
            the cipher expects to have 'encrypt' method only.

        :param 'displayName': str
            The cipher's name that is going to be shown in the ciphers'
            selection combo box.

        :param 'origin': str
            Name of the origin file. While creating a child class,
            send the '__name__' property to this argumen
            
        :kwparam 'category': str
            Name of the category the cipher belongs to. For example,
            there are hashes, simple cryptography methods like magic
            square, etc. Available categories are:
                'hash'   —— Hashing algorithms;
                'simple' —— Simple cryptography;
                'btte'   —— Binary-to-text encoding.

        :kwparam 'version': tuple<int, int>
            Version of the cipher
        '''
        self.type, self.displayName, self.origin, self.category, self.version = (
            type, displayName, f'{origin[8:]}.py', category, version)
        

    def getInformation(self, root: Window) -> str:
        '''
        Get a string representing cipher's properties to show it in 
        the UI.

        :returns: str
        '''
        translatedStrings = (
            root.translate('CiphersInfo', 'Category'),
            root.translate('CiphersInfo', 'Type'),
            root.translate('CiphersInfo', 'one-way'),
            root.translate('CiphersInfo', 'two-way'),
            root.translate('CiphersInfo', 'Defined in'),
            root.translate('CiphersInfo', 'Version'))

        return (
            f'{translatedStrings[0]}: {self.categories[self.category].text()}\n'
            f'{translatedStrings[1]}: {(translatedStrings[3] if self.type else translatedStrings[2])}\n'
            f'{translatedStrings[4]}: {self.origin}\n'
            f'{translatedStrings[5]}: {self.version[0]}.{self.version[1]}')


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
    print(638)
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
