from PySide6 import QtWidgets


class Settings(QtWidgets.QDialog):
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

