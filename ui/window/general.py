from PySide6 import QtWidgets


class Window(QtWidgets.QMainWindow):
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


