'Base* ciphers'

from main  import Cipher
from base64   import *
from binascii import Error as BaseCipherDecodingError

class Base16(Cipher):
    '''
    An implementation of the Base16 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base16', __name__, category = 'btte')


    def encrypt(self, text: str, encoding: str) -> str:
        result = b16encode(text.encode(encoding)).decode(encoding)
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str, encoding: str) -> str:
        try: return b16decode(text.encode(encoding)).decode(encoding)
        #simple fix of an incorrect padding error
        except BaseCipherDecodingError: return b16decode((text + '=').encode(encoding)).decode(encoding)


class Base32(Cipher):
    '''
    An implementation of the Base32 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base32', __name__, category = 'btte')


    def encrypt(self, text: str, encoding: str) -> str:
        result = b32encode(text.encode(encoding)).decode(encoding)
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str, encoding: str) -> str:
        try: return b32decode(text.encode(encoding)).decode(encoding)
        #simple fix of an incorrect padding error
        except BaseCipherDecodingError: return b32decode((text + '=').encode(encoding)).decode(encoding)


class Base64(Cipher):
    '''
    An implementation of the Base64 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base64', __name__, category = 'btte')


    def encrypt(self, text: str, encoding: str) -> str:
        result = b16encode(text.encode(encoding)).decode(encoding)
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str, encoding: str) -> str:
        try: return b16decode(text.encode(encoding)).decode(encoding)
        #simple fix of an incorrect padding error
        except BaseCipherDecodingError: return b16decode((text + '=').encode(encoding)).decode(encoding)


class Base85(Cipher):
    '''
    An implementation of the Base85 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base85', __name__, category = 'btte')


    def encrypt(self, text: str, encoding: str) -> str:
        result = b85encode(text.encode(encoding)).decode(encoding)
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str, encoding: str) -> str:
        try: return b85decode(text.encode(encoding)).decode(encoding)
        #simple fix of an incorrect padding error
        except BaseCipherDecodingError: return b85decode((text + '=').encode(encoding)).decode(encoding)
