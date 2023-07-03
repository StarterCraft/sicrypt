from PySide6 import QtWidgets


class PlainTextEdit(QtWidgets.QPlainTextEdit):
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
            {any > 0} —— corresponding spaces number.
        
        :returns: None    
        '''
        self.tabPolicy = policy


    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Tab and self.tabPolicy:
            QPlainTextEdit.keyPressEvent(self, QKeyEvent(
                QEvent.KeyPress, Qt.Key_Space,
                Qt.KeyboardModifiers(event.nativeModifiers()), ' ' * (self.tabPolicy + 1)))
        else: QPlainTextEdit.keyPressEvent(self, event)

