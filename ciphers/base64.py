from sicrypt import  Cipher
from base64  import (b64encode, b64decode)

#TODO No.2: Add Base16, Base32, Base85 implementation

class Base64(Cipher):
    '''
    An implementation of the Base64 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base64', 'btte')


    def encrypt(self, text: str) -> str:
        return b64encode(text.encode('utf-8')).decode('utf-8')


    def decrypt(self, text: str) -> str:
        return b64decode(text.encode('utf-8')).decode('utf-8')
