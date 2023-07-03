from PySide6 import QtGui


class Item(QtGui.QStandardItem):
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

