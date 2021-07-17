'Base* ciphers'

from sicrypt  import Cipher
from base64   import *
from binascii import Error as BaseCipherDecodingError


class Base16(Cipher):
    '''
    An implementation of the Base16 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base16', category = 'btte')


    def encrypt(self, text: str) -> str:
        result = b16encode(text.encode('utf-8')).decode('utf-8')
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str) -> str:
        try: return b16decode(text.encode('utf-8')).decode('utf-8')
        #simple fix of an incorrect padding error
        except BaseCipherDecodingError: return b16decode((text + '=').encode('utf-8')).decode('utf-8')


class Base32(Cipher):
    '''
    An implementation of the Base32 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base32', category = 'btte')


    def encrypt(self, text: str) -> str:
        result = b32encode(text.encode('utf-8')).decode('utf-8')
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str) -> str:
        try: return b32decode(text.encode('utf-8')).decode('utf-8')
        #simple fix of an incorrect padding error
        except BaseCipherDecodingError: return b32decode((text + '=').encode('utf-8')).decode('utf-8')


class Base64(Cipher):
    '''
    An implementation of the Base64 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base64', category = 'btte')


    def encrypt(self, text: str) -> str:
        result = b16encode(text.encode('utf-8')).decode('utf-8')
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str) -> str:
        try: return b16decode(text.encode('utf-8')).decode('utf-8')
        #simple fix of an incorrect padding error
        except BaseCipherDecodingError: return b16decode((text + '=').encode('utf-8')).decode('utf-8')


class Base85(Cipher):
    '''
    An implementation of the Base85 encoding algorythm.
    You can use this implementation as an example of a cipher implementation.
    '''
    def __init__(self):
        Cipher.__init__(self, True, 'Base85', category = 'btte')


    def encrypt(self, text: str) -> str:
        result = b85encode(text.encode('utf-8')).decode('utf-8')
        if result.endswith('='):
            firstEqSymbol = result.index('=')
            result = result[:-firstEqSymbol]
        return result


    def decrypt(self, text: str) -> str:
        try: return b85decode(text.encode('utf-8')).decode('utf-8')
        #simple fix of an incorrect padding error
        except BaseCipherDecodingError: return b85decode((text + '=').encode('utf-8')).decode('utf-8')
