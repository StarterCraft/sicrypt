# CHANGELOG
===
## 1.0
Initial version. Supported Base64 encryption only

## 1.1
First public version. The following features are introduced:
- Revamped UI now supports vertical and horizontal positioning of the text fields;
- Added support for multiple ciphering algorithms, named `ciphers` in the documentation, which can be downloaded from the program's GitHub or written by the user himself in Python;
- If some of the installed ciphers will be hosted on GitHub and will be outdated, they'll be updated;
- Added program configuration, the settings dialog and their dependencies (see documentation for details);
- Added file opening feature (open a file and paste its contents as source text). UTF-8 encoding is used by default, some other encodings can be specified via the button's popup menu;
- Added file saving feature (save result text into a file). UTF-8 encoding is used by default, some other encodings can be specified via the button's popup menu.

## 1.2
- It's now possible to specify encoding for encryption and decryption;
- Categorization is now implemented into the cipher selection combo box;
- Selected cipher's properties are now shown in the cipher selection combo box;
- It is now possible to select text fields for opening a file and saving into a file;
- Automatic updates are implemented

## 1.3
- It's now possible to switch the layout without rebooting;
- Fixed paste function failing due to an old variable name;
- Added support for latest Python versions and decreased the bundle size for installation;
- Added loading progress bar dialog on ciphers loading to remove the feeling of freezing on launch.
