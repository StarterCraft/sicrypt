
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
            root.translate('CipherInfo', 'Category'),
            root.translate('CipherInfo', 'Type'),
            root.translate('CipherInfo', 'one-way'),
            root.translate('CipherInfo', 'two-way'),
            root.translate('CipherInfo', 'Defined in'),
            root.translate('CipherInfo', 'Version'))

        return (
            f'{translatedStrings[0]}: {self.categories[self.category].text()}\n'
            f'{translatedStrings[1]}: {(translatedStrings[3] if self.type else translatedStrings[2])}\n'
            f'{translatedStrings[4]}: {self.origin}\n'
            f'{translatedStrings[5]}: {self.version[0]}.{self.version[1]}')
