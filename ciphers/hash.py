'Hashing alghorithms'

from sicrypt  import Cipher
from hashlib  import *

class MD5(Cipher):
    'A representation of a MD5 hashing algorythm'
    def __init__(self):
        Cipher.__init__(self, False, 'MD5',  __name__, category = 'hash')


    def encrypt(self, text: str, encoding: str) -> str:
        return md5(text.encode(encoding)).hexdigest()


class SHA224(Cipher):
    'A representation of a SHA224 hashing algorythm'
    def __init__(self):
        Cipher.__init__(self, False, 'SHA224',  __name__, category = 'hash')


    def encrypt(self, text: str, encoding: str) -> str:
        return sha224(text.encode(encoding)).hexdigest()


class SHA256(Cipher):
    'A representation of a SHA256 hashing algorythm'
    def __init__(self):
        Cipher.__init__(self, False, 'SHA256',  __name__, category = 'hash')


    def encrypt(self, text: str, encoding: str) -> str:
        return sha256(text.encode(encoding)).hexdigest()
