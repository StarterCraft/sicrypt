# Sicrypt
### EN-INT 
A light, handy, customizable, open-source cryptography tool

## Contents
1. [What is Sicrypt?](#About) 
2. [Features summary](#Usage) 
    1. [Encryption](#Encryption)
    2. [Decryption](#Decryption)
    3. [Opening a file](#Opening)
    4. [Saving into a file](#Saving)
    5. [Copying to the clipboard and pasting from it](#Copying&Pasting)
    6. [Trasferring text between the text fields](#Transferring)
    7. [Cofiguring the program](#Settings)
3. [Ciphers: creating your own, downloading](#Ciphers)

## About
Sicrypt is the ideal solution for encrypting and decrypting your text with any cipher you want, and you can even create your own cipher algorithm on Python very easily. By the way, the program can work offline, so you can replace your favorite web cryptography services with Sicrypt.
The solution will be very useful for people who work with cryptography every day, for programmers that work with cryptography in their projects, for people who want to experiment with cryptography to implement or in their life, etc.

The most important feature of Sicrypt is that you can implement your own cipher algorithm very easily, using Python programming language, even without having Python interpreter installed! See section 3 for more information about this.

If you have faced a critical error during usage of the program, please open an issue card with the details of the error, which you can copy from the error messagebox. If you would like to contribute to Sicrypt development, please start pull requests with your changes. 

## Usage
### Encryption
1. To encrypt some text, please place the text inside the *Source text* field.
2. Afterwards, please select a cipher in the *Cipher* combo box. 
3. After selecting the cipher, click the *Encrypt* button, and then the encrypted text will be shown in the *Result text* field.
![Description image](https://user-images.githubusercontent.com/43516901/125636677-776632ef-999a-4fe7-93b6-242f7fc34ed8.jpg)

### Decryption
1. To decrypt some text, please place the text inside the *Source text* field.
2. Afterwards, please select a cipher in the *Cipher* combo box. 
3. After selecting the cipher, click the *Decrypt* button, and then the encrypted text will be shown in the *Result text* field.
![Description image](https://user-images.githubusercontent.com/43516901/125637288-4f1ec6de-bc17-4f05-b460-ad95b2958b8b.jpg)

### Opening
You can open a text file to make its text appear inside of the *Source text* field.
By default, `UTF-8` encoding is used, but you can use the *Open file..* button popup menu actions to open a file with another encoding.
> TODO: add input dialog to enable the user to specify any valid encoding.
1. Click on the *Open file...* button or click on one of the actions inside of its popup menu. 
2. Select an existing file you want to open. 
3. After selecting the file, if opening succeeded, you can see the contents of the file in the *Source text* field.


### Saving 
