# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uisrc\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/zxc/icons/icon_-d.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLabel { \n"
"    color: white;\n"
"    font: 13pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QToolTip {\n"
"    color: white;\n"
"    font: 11pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    color: white;\n"
"    border: 1px solid grey;\n"
"    font: 12pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border-top: 1px solid white;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: rgb(59, 59, 59);\n"
"    border: 1px solid white;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding-left: 7px;\n"
"    padding-right: 7px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    font: 63 9pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QTabBar::tab:disabled { \n"
"    background-color: gray;\n"
"}\n"
"\n"
"QTabBar::tab:active:disabled {\n"
"    background-color: grey;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(47, 105, 23);\n"
"    color: rgb(248, 248, 248);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"    background-color: rgb(70, 175, 38);\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:hover { background-color: rgb(47, 105, 23); }\n"
"QListView::item:selected { background-color: rgb(70, 175, 38) }\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  rgb(70, 175, 38);\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { background-color: rgb(45, 102, 23); }\n"
"QSlider::handle:horizontal:disabled { background-color: grey; }\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"     background-color: rgb(45, 45, 45);         /* #605F5F; */\n"
"     min-height: 5px;\n"
"     border: 2px solid white;\n"
"     border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/icons/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/icons/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/icons/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/icons/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     background-color: #2A2929;    \n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"     background-color: rgb(45, 45, 45);      \n"
"     min-width: 5px;\n"
"     border: 2px solid white;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(./images/right_arrow_disabled.png);       \n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(./images/left_arrow_disabled.png);        \n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(./images/right_arrow.png);               \n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(./images/left_arrow.png);               \n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px green sunken;\n"
"}\n"
"\n"
"QSpinBox:disabled\n"
"{\n"
"    color: grey;\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"    color: white; \n"
"}\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"    color: white;\n"
"}\n"
"\n"
"QTimeEdit \n"
"{\n"
"    border: none;\n"
"    font: 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QTimeEdit:hover\n"
"{\n"
"    border: 1px green sunken;\n"
"}\n"
"\n"
"QTimeEdit:disabled\n"
"{\n"
"    color: grey; \n"
"}\n"
"\n"
"QTimeEdit::up-button\n"
"{\n"
"    color: white;\n"
"}\n"
"\n"
"QTimeEdit::down-button\n"
"{\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox \n"
"{\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: 11pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    border: 1px solid rgb(254, 254, 254);\n"
"    background-color: rgb(236, 236, 236);\n"
"}\n"
"\n"
"QComboBox:disabled\n"
"{\n"
"    color: gray;\n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/zxc/icons/arrowDown_ico.png);\n"
"}\n"
"\n"
"\n"
"QComboBox::up-arrow\n"
"{ \n"
"    image: url(:/zxc/icons/arrowUp_ico.png);\n"
"}\n"
"\n"
"\n"
"QComboBox:editable\n"
"{\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable\n"
"{\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"        stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on\n"
"{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"        stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{ /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    \n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    background-color: rgb(213, 213, 213); \n"
"    selection-background-color: rgb(70, 175, 38);\n"
"    \n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"    color: black;\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;  \n"
"    font: 11pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{ \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{ \n"
"    background-color: rgb(221, 221, 221);\n"
"}\n"
"\n"
"QToolButton\n"
"{ \n"
"    color: black;\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;  \n"
"    font: 11pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{ \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QToolButton:pressed\n"
"{ \n"
"    background-color: rgb(221, 221, 221);\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button\n"
"{\n"
"    border: 1px solid gray;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    background: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open\n"
"{\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"}\n"
"\n"
"QMenu \n"
"{\n"
"    background: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    font: 11pt \"Segoe UI Semilight\";\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QMenu::item:hover\n"
"{\n"
"    background: rgb(70, 175, 38);\n"
"    color: white;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background: rgb(47, 105, 23);\n"
"}\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: gray;\n"
"}\n"
"\n"
"QLineEdit\n"
"{ \n"
"    border-radius: 3px;\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{ \n"
"    border-color: rgb(42, 105, 23);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Encrypt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Encrypt.sizePolicy().hasHeightForWidth())
        self.btn_Encrypt.setSizePolicy(sizePolicy)
        self.btn_Encrypt.setMinimumSize(QtCore.QSize(150, 30))
        self.btn_Encrypt.setMaximumSize(QtCore.QSize(150, 30))
        self.btn_Encrypt.setShortcut("Ctrl+E")
        self.btn_Encrypt.setObjectName("btn_Encrypt")
        self.gridLayout.addWidget(self.btn_Encrypt, 5, 2, 1, 1)
        self.btn_Decrypt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Decrypt.sizePolicy().hasHeightForWidth())
        self.btn_Decrypt.setSizePolicy(sizePolicy)
        self.btn_Decrypt.setMinimumSize(QtCore.QSize(150, 30))
        self.btn_Decrypt.setMaximumSize(QtCore.QSize(150, 30))
        self.btn_Decrypt.setAutoFillBackground(False)
        self.btn_Decrypt.setShortcut("Ctrl+D")
        self.btn_Decrypt.setObjectName("btn_Decrypt")
        self.gridLayout.addWidget(self.btn_Decrypt, 6, 2, 1, 1)
        self.btn_TransferSrcToRes = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_TransferSrcToRes.sizePolicy().hasHeightForWidth())
        self.btn_TransferSrcToRes.setSizePolicy(sizePolicy)
        self.btn_TransferSrcToRes.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_TransferSrcToRes.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_TransferSrcToRes.setFont(font)
        self.btn_TransferSrcToRes.setStyleSheet("font-size: 16pt")
        self.btn_TransferSrcToRes.setIconSize(QtCore.QSize(16, 16))
        self.btn_TransferSrcToRes.setObjectName("btn_TransferSrcToRes")
        self.gridLayout.addWidget(self.btn_TransferSrcToRes, 6, 6, 1, 1)
        self.btn_Paste = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Paste.sizePolicy().hasHeightForWidth())
        self.btn_Paste.setSizePolicy(sizePolicy)
        self.btn_Paste.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_Paste.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_Paste.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/zxc/icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Paste.setIcon(icon1)
        self.btn_Paste.setIconSize(QtCore.QSize(22, 22))
        self.btn_Paste.setObjectName("btn_Paste")
        self.gridLayout.addWidget(self.btn_Paste, 5, 5, 1, 1)
        self.btn_TransferResToSrc = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_TransferResToSrc.sizePolicy().hasHeightForWidth())
        self.btn_TransferResToSrc.setSizePolicy(sizePolicy)
        self.btn_TransferResToSrc.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_TransferResToSrc.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_TransferResToSrc.setStyleSheet("font-size: 16pt")
        self.btn_TransferResToSrc.setObjectName("btn_TransferResToSrc")
        self.gridLayout.addWidget(self.btn_TransferResToSrc, 6, 5, 1, 1)
        self.lbl_ReadOnly2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ReadOnly2.setStyleSheet("font: 13pt \"Segoe UI Semibold\"")
        self.lbl_ReadOnly2.setObjectName("lbl_ReadOnly2")
        self.gridLayout.addWidget(self.lbl_ReadOnly2, 0, 3, 1, 2)
        self.btn_Settings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Settings.sizePolicy().hasHeightForWidth())
        self.btn_Settings.setSizePolicy(sizePolicy)
        self.btn_Settings.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_Settings.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_Settings.setStyleSheet("font-size: 12pt")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/zxc/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Settings.setIcon(icon2)
        self.btn_Settings.setIconSize(QtCore.QSize(20, 20))
        self.btn_Settings.setObjectName("btn_Settings")
        self.gridLayout.addWidget(self.btn_Settings, 0, 5, 1, 1)
        self.lbl_ReadOnly3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ReadOnly3.setObjectName("lbl_ReadOnly3")
        self.gridLayout.addWidget(self.lbl_ReadOnly3, 5, 0, 1, 2)
        self.tbt_SaveToFile = QtWidgets.QToolButton(self.centralwidget)
        self.tbt_SaveToFile.setMinimumSize(QtCore.QSize(150, 30))
        self.tbt_SaveToFile.setMaximumSize(QtCore.QSize(150, 30))
        self.tbt_SaveToFile.setStyleSheet("padding-right: 20px;")
        self.tbt_SaveToFile.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.tbt_SaveToFile.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbt_SaveToFile.setAutoRaise(False)
        self.tbt_SaveToFile.setObjectName("tbt_SaveToFile")
        self.gridLayout.addWidget(self.tbt_SaveToFile, 6, 3, 1, 1)
        self.tbt_OpenFile = QtWidgets.QToolButton(self.centralwidget)
        self.tbt_OpenFile.setMinimumSize(QtCore.QSize(150, 30))
        self.tbt_OpenFile.setMaximumSize(QtCore.QSize(150, 30))
        self.tbt_OpenFile.setStyleSheet("padding-right: 20px;")
        self.tbt_OpenFile.setIconSize(QtCore.QSize(16, 16))
        self.tbt_OpenFile.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.tbt_OpenFile.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbt_OpenFile.setAutoRaise(False)
        self.tbt_OpenFile.setObjectName("tbt_OpenFile")
        self.gridLayout.addWidget(self.tbt_OpenFile, 5, 3, 1, 1)
        self.cbb_Cipher = QtWidgets.QComboBox(self.centralwidget)
        self.cbb_Cipher.setMinimumSize(QtCore.QSize(0, 30))
        self.cbb_Cipher.setObjectName("cbb_Cipher")
        self.gridLayout.addWidget(self.cbb_Cipher, 6, 0, 1, 2)
        self.ptx_SourceText = PlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ptx_SourceText.sizePolicy().hasHeightForWidth())
        self.ptx_SourceText.setSizePolicy(sizePolicy)
        self.ptx_SourceText.setMaximumSize(QtCore.QSize(290, 16777215))
        self.ptx_SourceText.setStyleSheet("QPlianTextEdit::placeholder-text { color: lightgray; }")
        self.ptx_SourceText.setObjectName("ptx_SourceText")
        self.gridLayout.addWidget(self.ptx_SourceText, 4, 0, 1, 3)
        self.lbl_ReadOnly1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_ReadOnly1.setFont(font)
        self.lbl_ReadOnly1.setStyleSheet("font: 13pt \"Segoe UI Semibold\"")
        self.lbl_ReadOnly1.setObjectName("lbl_ReadOnly1")
        self.gridLayout.addWidget(self.lbl_ReadOnly1, 0, 0, 1, 3)
        self.btn_About = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_About.sizePolicy().hasHeightForWidth())
        self.btn_About.setSizePolicy(sizePolicy)
        self.btn_About.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_About.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_About.setStyleSheet("font-size: 13pt")
        self.btn_About.setObjectName("btn_About")
        self.gridLayout.addWidget(self.btn_About, 0, 6, 1, 1)
        self.btn_Copy = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Copy.sizePolicy().hasHeightForWidth())
        self.btn_Copy.setSizePolicy(sizePolicy)
        self.btn_Copy.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_Copy.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_Copy.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/zxc/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Copy.setIcon(icon3)
        self.btn_Copy.setIconSize(QtCore.QSize(20, 20))
        self.btn_Copy.setObjectName("btn_Copy")
        self.gridLayout.addWidget(self.btn_Copy, 5, 6, 1, 1)
        self.ptx_ResultText = PlainTextEdit(self.centralwidget)
        self.ptx_ResultText.setMaximumSize(QtCore.QSize(290, 16777215))
        self.ptx_ResultText.setObjectName("ptx_ResultText")
        self.gridLayout.addWidget(self.ptx_ResultText, 4, 3, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sicrypt"))
        self.btn_Encrypt.setToolTip(_translate("MainWindow", "Encrypt source text"))
        self.btn_Encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_Decrypt.setToolTip(_translate("MainWindow", "Decrypt source text"))
        self.btn_Decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_TransferSrcToRes.setToolTip(_translate("MainWindow", "Tansfer contents of \'Source text\' field to \'Result text\' field"))
        self.btn_TransferSrcToRes.setText(_translate("MainWindow", "🠖"))
        self.btn_Paste.setToolTip(_translate("MainWindow", "Paste clipboard text as source text"))
        self.btn_TransferResToSrc.setToolTip(_translate("MainWindow", "Tansfer contents of \'Result text\' field to \'Source text\' field"))
        self.btn_TransferResToSrc.setText(_translate("MainWindow", "🠔"))
        self.lbl_ReadOnly2.setText(_translate("MainWindow", "Result text:"))
        self.btn_Settings.setToolTip(_translate("MainWindow", "Settings"))
        self.lbl_ReadOnly3.setText(_translate("MainWindow", "Cipher:"))
        self.tbt_SaveToFile.setToolTip(_translate("MainWindow", "Save result text to a file"))
        self.tbt_SaveToFile.setText(_translate("MainWindow", "Save to file..."))
        self.tbt_OpenFile.setToolTip(_translate("MainWindow", "Open a file and paste its contents as source text"))
        self.tbt_OpenFile.setText(_translate("MainWindow", "Open file..."))
        self.cbb_Cipher.setToolTip(_translate("MainWindow", "Select your cipher"))
        self.ptx_SourceText.setPlaceholderText(_translate("MainWindow", "Type or paste in source text"))
        self.lbl_ReadOnly1.setText(_translate("MainWindow", "Source text:"))
        self.btn_About.setToolTip(_translate("MainWindow", "Help/About"))
        self.btn_About.setText(_translate("MainWindow", "?"))
        self.btn_Copy.setToolTip(_translate("MainWindow", "Copy result text to the clipboard"))
        self.ptx_ResultText.setPlaceholderText(_translate("MainWindow", "En- or decrypted text will appear here"))
from sicrypt import PlainTextEdit
import res_rc
