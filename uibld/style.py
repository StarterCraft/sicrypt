styleSheet = '''QListView, QTreeView, QColumnView, QLabel, QLineEdit, QComboBox, QToolTip { 
    color: white;
    font: 9pt "Segoe UI"; 
}

QLineEdit, QComboBox {
    color: white;
    font: 9pt "Segoe UI";
    border: 1px solid white;
    border-radius: 2px;
}

QListView, QTreeView {
    color: white;
    font: 9pt "Segoe UI"; 
    show-decoration-selected: 1;
}

QListView::item:hover, QTreeView::item:hover {
    background-color:rgb(70, 175, 38);
}

QListView::item:selected, QTreeView::item:selected {
    background-color: rgb(47, 105, 23); 
}

QPushButton { 
	color: black;
    background-color: rgb(215, 215, 215);
	border: 1px solid gray;
	border-radius: 3px;  
	min-width: 6em;
    padding: 1px 5px 1px 5px;
	font: 8pt "Segoe UI Semibold";
}


QPushButton:hover { 
	background-color: rgb(235, 235, 235);
}


QPushButton:pressed { 
	background-color: rgb(221, 221, 221);
}

QScrollBar:vertical, QScrollBar:horizontal 
{
    background-color: #2A2929;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border: 1px transparent #2A2929;
}


QScrollBar::handle:vertical, QScrollBar::handle:horizontal 
{
    background-color: rgb(45, 45, 45);         /* #605F5F; */
    min-height: 5px;
    border: 2px solid white;
	border-radius: 4px;
}


QScrollBar::sub-line:vertical, QScrollBar::sub-line:horizontal 
{
    margin: 3px 0px 3px 0px;
    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical, QScrollBar::add-line:horizontal
{
    margin: 3px 0px 3px 0px;
    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}


QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on, QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
{
    border-image: url(:/qss_icons/rc/up_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on, QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on
{
    border-image: url(:/qss_icons/rc/down_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}


QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,  QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal 
{
    background: none;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical, QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;
}

QListWidget::item {
    color: white;
}
'''


buttonStyleSheet = '''color: black;
    background-color: rgb(215, 215, 215);
	border: 1px solid gray;
	border-radius: 3px;  
	min-width: 6em;
    padding: 1px 5px 1px 5px;
	font: 8pt "Segoe UI Semibold";
'''


appStyleSheet = '''QMenu 
{
    background: rgb(215, 215, 215);
    border: 1px solid gray;
}

QMenu::item {
    font: 11pt "Segoe UI Semilight";
    padding-left: 2px;
    padding-right: 25px;
}

QMenu::item:hover
{
    background: rgb(70, 175, 38);
    color: white;
}

QMenu::item:selected
{
    background: rgb(47, 105, 23);
}

QMenu::item:disabled
{
    color: gray;
}
'''
