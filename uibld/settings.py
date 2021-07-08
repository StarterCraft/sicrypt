# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uisrc\settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(450, 380))
        Dialog.setMaximumSize(QtCore.QSize(450, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/zxc/icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(45, 45, 45)")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("QLabel { \n"
"    color: white;\n"
"    font: 13pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    color: white;\n"
"    font: 11pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/zxc/icons/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(:/zxc/icons/checkbox_checked_hover.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/zxc/icons/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(:/zxc/icons/checkbox_unchecked_hover.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/zxc/icons/radiobutton_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(:/zxc/icons/radiobutton_checked_hover.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/zxc/icons/radiobutton_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(:/zxc/icons/radiobutton_unchecked_hover.png);\n"
"}\n"
"\n"
"QCheckBox:disabled, QRadioButton:disabled {\n"
"    color: gray;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    color: white;\n"
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
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
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
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: rgb(47, 105, 23);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: rgb(70, 175, 38);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  rgb(70, 175, 38);\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(45, 102, 23);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background-color: grey;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
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
"QSpinBox\n"
"{\n"
"    color: black;\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;  \n"
"    font: 11pt \"Segoe UI Semilight\";\n"
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
"    color: black;\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox::down-button\n"
"{   \n"
"    color: black;\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QTimeEdit \n"
"{\n"
"    border: none;\n"
"    font: 11pt \"Segoe UI\";\n"
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
"    min-width: 6em;\n"
"    font: 11pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    border: 1px solid rgb(254, 254, 254);\n"
"    background-color: rgb(236, 236, 236);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    border: 2px solid darkgray;\n"
"    background-color: rgb(213, 213, 213); \n"
"    selection-background-color: rgb(70, 175, 38);\n"
"}\n"
"\n"
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
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
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_ReadOnly4 = QtWidgets.QLabel(self.frame)
        self.lbl_ReadOnly4.setStyleSheet("font-family: Segoe UI Semibold")
        self.lbl_ReadOnly4.setObjectName("lbl_ReadOnly4")
        self.gridLayout.addWidget(self.lbl_ReadOnly4, 5, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.lbl_ReadOnly6 = QtWidgets.QLabel(self.frame)
        self.lbl_ReadOnly6.setObjectName("lbl_ReadOnly6")
        self.gridLayout.addWidget(self.lbl_ReadOnly6, 8, 0, 1, 1)
        self.cbb_Language = QtWidgets.QComboBox(self.frame)
        self.cbb_Language.setMinimumSize(QtCore.QSize(143, 0))
        self.cbb_Language.setMaximumSize(QtCore.QSize(256, 16777215))
        self.cbb_Language.setObjectName("cbb_Language")
        self.cbb_Language.addItem("")
        self.gridLayout.addWidget(self.cbb_Language, 3, 1, 1, 2)
        self.lbl_ReadOnly1 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ReadOnly1.sizePolicy().hasHeightForWidth())
        self.lbl_ReadOnly1.setSizePolicy(sizePolicy)
        self.lbl_ReadOnly1.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_ReadOnly1.setFont(font)
        self.lbl_ReadOnly1.setStyleSheet("font-family: Segoe UI Black")
        self.lbl_ReadOnly1.setObjectName("lbl_ReadOnly1")
        self.gridLayout.addWidget(self.lbl_ReadOnly1, 0, 0, 1, 3)
        self.lbl_ReadOnly7 = QtWidgets.QLabel(self.frame)
        self.lbl_ReadOnly7.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lbl_ReadOnly7.setObjectName("lbl_ReadOnly7")
        self.gridLayout.addWidget(self.lbl_ReadOnly7, 9, 0, 1, 1)
        self.cbb_Font = QtWidgets.QFontComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbb_Font.sizePolicy().hasHeightForWidth())
        self.cbb_Font.setSizePolicy(sizePolicy)
        self.cbb_Font.setMinimumSize(QtCore.QSize(143, 0))
        self.cbb_Font.setMaximumSize(QtCore.QSize(210, 16777215))
        self.cbb_Font.setIconSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        self.cbb_Font.setCurrentFont(font)
        self.cbb_Font.setObjectName("cbb_Font")
        self.gridLayout.addWidget(self.cbb_Font, 8, 1, 1, 1)
        self.lbl_ReadOnly8 = QtWidgets.QLabel(self.frame)
        self.lbl_ReadOnly8.setObjectName("lbl_ReadOnly8")
        self.gridLayout.addWidget(self.lbl_ReadOnly8, 11, 0, 1, 1)
        self.lbl_ReadOnly3 = QtWidgets.QLabel(self.frame)
        self.lbl_ReadOnly3.setObjectName("lbl_ReadOnly3")
        self.gridLayout.addWidget(self.lbl_ReadOnly3, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 3)
        self.spb_FontSize = QtWidgets.QSpinBox(self.frame)
        self.spb_FontSize.setMaximumSize(QtCore.QSize(35, 16777215))
        self.spb_FontSize.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spb_FontSize.setProperty("value", 13)
        self.spb_FontSize.setObjectName("spb_FontSize")
        self.gridLayout.addWidget(self.spb_FontSize, 8, 2, 1, 1)
        self.lbl_ReadOnly2 = QtWidgets.QLabel(self.frame)
        self.lbl_ReadOnly2.setStyleSheet("font-family: Segoe UI Semibold")
        self.lbl_ReadOnly2.setObjectName("lbl_ReadOnly2")
        self.gridLayout.addWidget(self.lbl_ReadOnly2, 2, 0, 1, 1)
        self.lbl_ReadOnly5 = QtWidgets.QLabel(self.frame)
        self.lbl_ReadOnly5.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lbl_ReadOnly5.setObjectName("lbl_ReadOnly5")
        self.gridLayout.addWidget(self.lbl_ReadOnly5, 6, 0, 1, 1)
        self.frame_WordWrapSelectors = QtWidgets.QFrame(self.frame)
        self.frame_WordWrapSelectors.setMaximumSize(QtCore.QSize(16777215, 26))
        self.frame_WordWrapSelectors.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_WordWrapSelectors.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_WordWrapSelectors.setObjectName("frame_WordWrapSelectors")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_WordWrapSelectors)
        self.horizontalLayout.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ckb_ResultTextFieldTextWrap = QtWidgets.QCheckBox(self.frame_WordWrapSelectors)
        self.ckb_ResultTextFieldTextWrap.setChecked(True)
        self.ckb_ResultTextFieldTextWrap.setObjectName("ckb_ResultTextFieldTextWrap")
        self.horizontalLayout.addWidget(self.ckb_ResultTextFieldTextWrap)
        self.ckb_SourceTextFieldTextWrap = QtWidgets.QCheckBox(self.frame_WordWrapSelectors)
        self.ckb_SourceTextFieldTextWrap.setObjectName("ckb_SourceTextFieldTextWrap")
        self.horizontalLayout.addWidget(self.ckb_SourceTextFieldTextWrap)
        self.gridLayout.addWidget(self.frame_WordWrapSelectors, 9, 1, 1, 2)
        self.tbs_TabPolicyFieldsSelector = QtWidgets.QTabWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbs_TabPolicyFieldsSelector.sizePolicy().hasHeightForWidth())
        self.tbs_TabPolicyFieldsSelector.setSizePolicy(sizePolicy)
        self.tbs_TabPolicyFieldsSelector.setMinimumSize(QtCore.QSize(0, 55))
        self.tbs_TabPolicyFieldsSelector.setMaximumSize(QtCore.QSize(16777215, 64))
        self.tbs_TabPolicyFieldsSelector.setObjectName("tbs_TabPolicyFieldsSelector")
        self.tab_SourceTextFieldTabPolicy = QtWidgets.QWidget()
        self.tab_SourceTextFieldTabPolicy.setObjectName("tab_SourceTextFieldTabPolicy")
        self.cbb_SourceTextFieldTabPolicy = QtWidgets.QComboBox(self.tab_SourceTextFieldTabPolicy)
        self.cbb_SourceTextFieldTabPolicy.setGeometry(QtCore.QRect(0, 0, 251, 26))
        self.cbb_SourceTextFieldTabPolicy.setMinimumSize(QtCore.QSize(143, 0))
        self.cbb_SourceTextFieldTabPolicy.setMaximumSize(QtCore.QSize(256, 16777215))
        self.cbb_SourceTextFieldTabPolicy.setObjectName("cbb_SourceTextFieldTabPolicy")
        self.cbb_SourceTextFieldTabPolicy.addItem("")
        self.cbb_SourceTextFieldTabPolicy.addItem("")
        self.cbb_SourceTextFieldTabPolicy.addItem("")
        self.cbb_SourceTextFieldTabPolicy.addItem("")
        self.tbs_TabPolicyFieldsSelector.addTab(self.tab_SourceTextFieldTabPolicy, "")
        self.tab_ResultTextFieldTabPolicy = QtWidgets.QWidget()
        self.tab_ResultTextFieldTabPolicy.setObjectName("tab_ResultTextFieldTabPolicy")
        self.cbb_ResultTextFieldTabPolicy = QtWidgets.QComboBox(self.tab_ResultTextFieldTabPolicy)
        self.cbb_ResultTextFieldTabPolicy.setGeometry(QtCore.QRect(0, 0, 230, 26))
        self.cbb_ResultTextFieldTabPolicy.setMinimumSize(QtCore.QSize(143, 0))
        self.cbb_ResultTextFieldTabPolicy.setMaximumSize(QtCore.QSize(230, 16777215))
        self.cbb_ResultTextFieldTabPolicy.setObjectName("cbb_ResultTextFieldTabPolicy")
        self.cbb_ResultTextFieldTabPolicy.addItem("")
        self.cbb_ResultTextFieldTabPolicy.addItem("")
        self.cbb_ResultTextFieldTabPolicy.addItem("")
        self.cbb_ResultTextFieldTabPolicy.addItem("")
        self.tbs_TabPolicyFieldsSelector.addTab(self.tab_ResultTextFieldTabPolicy, "")
        self.gridLayout.addWidget(self.tbs_TabPolicyFieldsSelector, 11, 1, 1, 2)
        self.frame_TextFieldsPosition = QtWidgets.QFrame(self.frame)
        self.frame_TextFieldsPosition.setMaximumSize(QtCore.QSize(16777215, 26))
        self.frame_TextFieldsPosition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TextFieldsPosition.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TextFieldsPosition.setObjectName("frame_TextFieldsPosition")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_TextFieldsPosition)
        self.horizontalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rbt_TextFieldsPositionHorizontal = QtWidgets.QRadioButton(self.frame_TextFieldsPosition)
        self.rbt_TextFieldsPositionHorizontal.setObjectName("rbt_TextFieldsPositionHorizontal")
        self.horizontalLayout_2.addWidget(self.rbt_TextFieldsPositionHorizontal)
        self.rbt_TextFieldsPositionVertical = QtWidgets.QRadioButton(self.frame_TextFieldsPosition)
        self.rbt_TextFieldsPositionVertical.setCheckable(True)
        self.rbt_TextFieldsPositionVertical.setChecked(True)
        self.rbt_TextFieldsPositionVertical.setObjectName("rbt_TextFieldsPositionVertical")
        self.horizontalLayout_2.addWidget(self.rbt_TextFieldsPositionVertical)
        self.gridLayout.addWidget(self.frame_TextFieldsPosition, 6, 1, 1, 2)
        self.verticalLayout_4.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("QPushButton\n"
"{ \n"
"    color: black;\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    min-width: 80px;\n"
"    min-height: 30px;\n"
"    padding: 0px 4px 0px 4px;\n"
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
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tbs_TabPolicyFieldsSelector.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sicrypt Settings"))
        self.lbl_ReadOnly4.setText(_translate("Dialog", "Text fields\' appearance:"))
        self.lbl_ReadOnly6.setText(_translate("Dialog", "Font:"))
        self.cbb_Language.setItemText(0, _translate("Dialog", "English"))
        self.lbl_ReadOnly1.setText(_translate("Dialog", "Settings"))
        self.lbl_ReadOnly7.setText(_translate("Dialog", "Word wrap:"))
        self.lbl_ReadOnly8.setText(_translate("Dialog", "Tab policy:"))
        self.lbl_ReadOnly3.setText(_translate("Dialog", "Language:"))
        self.lbl_ReadOnly2.setText(_translate("Dialog", "General:"))
        self.lbl_ReadOnly5.setText(_translate("Dialog", "Position:"))
        self.ckb_ResultTextFieldTextWrap.setText(_translate("Dialog", "Result text"))
        self.ckb_SourceTextFieldTextWrap.setText(_translate("Dialog", "Source text"))
        self.cbb_SourceTextFieldTabPolicy.setItemText(0, _translate("Dialog", "Tab symbol"))
        self.cbb_SourceTextFieldTabPolicy.setItemText(1, _translate("Dialog", "2 spaces"))
        self.cbb_SourceTextFieldTabPolicy.setItemText(2, _translate("Dialog", "3 spaces"))
        self.cbb_SourceTextFieldTabPolicy.setItemText(3, _translate("Dialog", "4 spaces"))
        self.tbs_TabPolicyFieldsSelector.setTabText(self.tbs_TabPolicyFieldsSelector.indexOf(self.tab_SourceTextFieldTabPolicy), _translate("Dialog", " Source text "))
        self.cbb_ResultTextFieldTabPolicy.setItemText(0, _translate("Dialog", "Tab как символ"))
        self.cbb_ResultTextFieldTabPolicy.setItemText(1, _translate("Dialog", "2 пробела"))
        self.cbb_ResultTextFieldTabPolicy.setItemText(2, _translate("Dialog", "3 пробела"))
        self.cbb_ResultTextFieldTabPolicy.setItemText(3, _translate("Dialog", "4 пробела"))
        self.tbs_TabPolicyFieldsSelector.setTabText(self.tbs_TabPolicyFieldsSelector.indexOf(self.tab_ResultTextFieldTabPolicy), _translate("Dialog", " Result text"))
        self.rbt_TextFieldsPositionHorizontal.setText(_translate("Dialog", "Horizontal"))
        self.rbt_TextFieldsPositionVertical.setText(_translate("Dialog", "Vertical"))
import res_rc