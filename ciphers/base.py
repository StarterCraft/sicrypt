'Base* ciphers'

from sicrypt  import Cipher
from base64   import *
from binascii import Error as Base64DecodingError

#TODO No.2: Add Base16, Base32, Base85 implementation

class Base64(Cipher):
    '''
    An implementation of the Base64 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base64', category = 'btte')


    def encrypt(self, text: str) -> str:
        result = b64encode(text.encode('utf-8')).decode('utf-8')
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str) -> str:
        try: return b64decode(text.encode('utf-8')).decode('utf-8')
        #simple fix of an incorrect padding error
        except Base64DecodingError: return b64decode((text + '=').encode('utf-8')).decode('utf-8')
