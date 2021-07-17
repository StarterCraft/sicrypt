'Hashing alghorithms'

from sicrypt  import Cipher
from hashlib  import *

class MD5(Cipher):
    'A representation of a MDP hashing algorythm'
    def __init__(self):
        Cipher.__init__(self, False, 'MD5',  __name__, category = 'hash')


    def encrypt(self, text: str, encoding: str) -> str:
        return md5(text.encode(encoding)).hexdigest()
