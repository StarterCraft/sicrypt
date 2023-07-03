from PySide6 import QtGui


class Action(QtGui.QAction):
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

