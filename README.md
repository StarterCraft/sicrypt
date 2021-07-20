# Sicrypt
### Languages / Языки
- [English (International)](#EN-INT)
- [Russian (Russian Federation](#RU-RU)

### EN-INT
A light, handy, customizable, open-source cryptography tool

## Contents
1. [What is Sicrypt?](#About)
2. [Built with...](#Used)
3. [Installation](#Installation)
4. [Features summary](#Usage) 
    1. [Encryption](#Encryption)
    2. [Decryption](#Decryption)
    3. [Opening a file](#Opening)
    4. [Saving into a file](#Saving)
    5. [Copying to the clipboard and pasting from it](#Copying&Pasting)
    6. [Trasferring text between the text fields](#Transferring)
    7. [Cofiguring the program](#Settings)
5. [Ciphers](#Ciphers)
    1. [Downloading ciphers](#Downloading)
    2. [Creating your own cipher](#Creating)

## About
![Image](https://user-images.githubusercontent.com/43516901/126315183-95e3296a-fbac-43ba-8d15-742001dbace8.png)
Sicrypt is the ideal solution for encrypting and decrypting your text with any cipher you want, and you can even create your own cipher algorithm on Python very easily. By the way, the program can work offline, so you can replace your favorite web cryptography services with Sicrypt.
The solution will be very useful for people who work with cryptography every day, for programmers that work with cryptography in their projects, for people who want to experiment with cryptography to implement or in their life, etc.

The most important feature of Sicrypt is that you can implement your own cipher algorithm very easily, using Python programming language, even without having Python interpreter installed! See section 3 for more information about this.

If you have faced a critical error during usage of the program, please open an issue card with the details of the error, which you can copy from the error messagebox. If you would like to contribute to Sicrypt development, please start pull requests with your changes. 

## Used
- Python 3.8.2
- PyQt5 5.15.2
- [pyperclip](https://github.com/asweigart/pyperclip)
- [requests](https://github.com/psf/requests)

## Installation
1. [Download](https://github.com/StarterCraft/sicrypt/releases/latest) the latest release.
2. Follow the installation guidance below:
    - For versions 1.1 and 1.2, please specify the installation folder and click *Start*.
        
## Usage
### Encryption
1. To encrypt some text, please place the text inside the *Source text* field.
2. Afterwards, please select a cipher in the *Cipher* combo box.
3. After selecting the cipher, click the *Encrypt* button, and then the encrypted text will be shown in the *Result text* field. By default,   
`UTF-8` encoding is used, but you can use the *Encrypt* button popup menu actions to open a file with another encoding, you can also use *Other...* menu action to specify your own encoding.

### Decryption
1. To decrypt some text, please place the text inside the *Source text* field.
2. Afterwards, please select a cipher in the *Cipher* combo box. 
3. After selecting the cipher, click the *Decrypt* button, and then the encrypted text will be shown in the *Result text* field. By default,  
`UTF-8` encoding is used, but you can use the *Decrypt* button popup menu actions to open a file with another encoding, you can also use *Other...* menu action to specify your own encoding.

### Opening
You can open a text file to make its text appear inside of the *Source text* field.
By default, `UTF-8` encoding is used, but you can use the *Open file...* button popup menu actions to open a file with another encoding, you can also use *Other...* menu action to specify your own encoding.
1. Select the text field you want to see the contents of the file in the *Open file...* button popup menu. 
2. Click on the *Open file...* button or click on one of the encoding-related actions inside of its popup menu. 
3. Select an existing file you want to open. 
4. After selecting the file, if opening succeeded, you can see the contents of the file in the specified field.

### Saving 
You can create or overwrite a file to save the contents of the *Result text* field into it.
By default, `UTF-8` encoding is used, but you can use the *Save to file...* button popup menu actions to save to a file with another encoding, you can also use *Other...* menu action to specify your own encoding.
1. Select the text field, which contents you want to see in the saved file in the *Save to file...* button popup menu..
1. Click on the *Save to file...* button or click on one of the actions inside of its popup menu. 
2. Select any file you want to save to; if the specified file exists, you'll be asked if you wish to overwrite it. 
3. After selecting the file, if saving succeeded, you can see the contents of your specified field in your specified file.

### Copying&Pasting
- You can paste the contents of your clipboard (please ensure the contents can be interpreted as text) to the *Source text* field. To do so, please click on the *Paste* button in the bottom right corner, which is shown as a standard pasting symbol (like 📋).
- You can copy the contents of the *Result text* field into your clipboard. To do so, please click on the *Copy* button in the bottom right corner, which is shown as a standard copying symbol (like 📄).

### Transferring
You can transfer the contents of *Source text* and *Result text* fields between them. To do so, please use buttons in the bottom right corner, which are shown as arrows facing the transfer direction. While using *Vertical* (default) or *Horizontal* layouts of the text fields, the direction of the arrows will change correspondingly.

### Settings
The configuration options and the possible values are listed in the table below.
`F` prefix in the option name means that the option is configured separately for each text field.

#### General options
**Option name** | **Possible values** | **Remarks** | 
--- | --- | --- |
*Language* | English | No localization support implemented yet | 

#### Encryption options
**Option name** | **Possible values** | **Remarks** | 
--- | --- | --- |
*Update installed ciphers if there are any updates* | Yes/No | Should the installed ciphers, if these are hosted on our GitHub, be redownloaded if there is a newer version on GitHub? |
| *Download new ciphers if there are any* | Yes/No | Should ciphers present on our GitHub, but unpresent in the local `ciphers` folder, be downloaded? |

#### Text fields' appearance options
**Option name** | **Possible values** | **Remarks** | 
--- | --- | --- |
*Position* | Vertical/Horizontal | How should the border between the text fields be positioned? |
`F` *Font* | `InstalledFont` & `int<8, 99>` | Which font family & font size must be used in the specified text field? |
`F` *Tab policy* | Tab symbol/2 spaces/3 spaces/4 spaces | Which character(s) must be inserted while `Tab` key is pressed in the specified text field?
`F` *Line wrap* | Yes/No | Must the lines be wrapped in the specified text field?

### Ciphers
Ciphers are represented as `.py` files stored in the `ciphers` directory at the program's location. Inside of such a file there is a defined class, inherited from [`Cipher`](https://github.com/StarterCraft/sicrypt/blob/master/sicrypt.py#L397) class.

Ciphers can be monodirectional (encryption-only, like hashing alghorythms) and bidirectional (encryption and decryption). They have categories, like *Binary-to-text-encoding*, (more information about categorization see in the class documentation) and a display name, which is shown in the cipher selection combo box.

#### Downloading
Sicrypt automatically tries to download all ciphers hosted on this GitHub repository on first launch. As stated in [**Settings**](#Settings) section, you can switch on and off the ciphers' downloading from GitHub. But with ciphers' downloading turned on, you don't need to manually download ciphers for Sicrypt, it'll do it itself. In case of no Internet connection available, you might need to define the ciphers yourself (see the next section for more info).

#### Creating
To create a cipher, you need to create a `{fileName}.py` file in the `ciphers` directory. You can use the template and guidance below to define your ciphers, by the way you can define as many ciphers in one file as you want, and as many cipher definition files as you want. See also [`Cipher` class documentation](https://github.com/StarterCraft/sicrypt/blob/master/sicrypt.py#L397).

```python
#Always import 'Cipher' class!
from sicrypt  import Cipher

#Import libraries if necessary for your cipher definition 
from base64   import *
from binascii import Error as BaseCipherDecodingError

#Define a class inheriting 'Cipher' class
class MyCipher(Cipher):
    '''
    Write a brief description of your cipher.
    '''
    def __init__(self):
        #Initialize a Cipher instance (more parameters related info can be found
        #in the Cipher class documentation)
        #Cipher.__init__(self, type: bool (False -> Monodirectional/True -> Bidirectional),
            displayName: str, __name__, category: str)
        Cipher.__init__(self, True, 'MyTestCipher', __name__, 'btte')


    #Every class inherited from `Cipher` class must have an `encrypt` method,
    #and, in case of bidirectional cipher, a `decrypt` method. Each method
    #must accept two string arguments (text to encrypt/decrypt, encoding) and
    #return a string.
    def encrypt(self, text: str, encoding: str) -> str:
        #Do some cryptography-related routine here
        s = f'MyText: {text}'
        return s


    #The method below must be defined in case of a bidirectional cipher
    def decrypt(self, text: str, encoding: str) -> str:
        #Do some cryptography-related routine here
        s = f'MyText: {text}'
        return s
```
