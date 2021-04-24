# AES-python
AES with encryption and decryption for files using 128 bit key size

Project developed with Python version 3.6.8 and numpy version 1.18.1

You can find an encryption key and files to be encrypted in the file fot test directory.

## How to use it

### Create a file for the key
First, you need to create a texte file and write your key in it:
![cle.txt](https://github.com/NorianGuernine/AES-python/blob/main/Pictures/cle_txt.png)

Please be careful not to add more than one space between each byte of the key.
There should be no space before the first byte or after the last byte. 

### Launch main.pyw
Then launch the file main.pyw and click on "ouvrir" in the frame "Clé de chiffrement"
You can check if your key loaded correctly in the "key value (decimal)" Entry box
![chargement_cle](https://github.com/NorianGuernine/AES-python/blob/main/Pictures/cle_main.png)

#### Encrypt file
To encrypt an file, go to the "Chiffrement" frame.
If your file is of binary type (such as png files) check the box "Fichier binaire", else, leave the box empty. 
After that, click on "Ouvrir" and select your file, then, click on "Chiffrer" and choose where to save the encrypted file.
When the encryption is complete, a binary file is created, this is your encrypted file.

#### Decrypt file 
To decrypt file, go to the "Déchiffrement" frame.
If your file is of binary type (such as pictures) check the box "Fichier binaire", else, leave the box empty. 
After that, click on "Ouvrir" and select the file corresponding to the encrypted file, then, click on "Déchiffrer" and choose were to save the decrypted file. /!\ You must specify the extension of your file when you save it.

## Code structure
You can find the code in the src folder

### CF_Multi.py
Multiplication by Galois field for MixColumns functions 

### Chiffrement_AES.py
Rijndael encryption functions 

### crypt_decrypt_fichier
Functions to encrypt and decrypt files

### Dechiffrement_AES.py
Rijndael decryption functions 

### main.py
User interface to encrypt and decrypt files

### Matrices.py
Contain the Sbox, InvSbox and Rcon matrix

### MiseEnForme.py
Contain functions to convert String to list and list to numpy array with type uint8

### Operation_cle.py
AddRounkey operation, Keyschedule and KeyExpansion to calculate new key for each round

## About the cipher
The padding used is PKCS#7.

The next updates will add other block cipher mode of operation such as CBC and CFB mode.

