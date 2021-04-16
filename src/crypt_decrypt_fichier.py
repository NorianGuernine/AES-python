# -*- coding: utf-8 -*-
#Chiffrement fichier

import numpy as np
from MiseEnForme import *
from Operation_cle import KeyExpansion
from Chiffrement_AES import Rijndael, envoi_crypto
from Dechiffrement_AES import InvRijndael, recoi_decrypt
from Matrices import Sbox, Rcon
import csv

def ecriture_ciphertext(fichier_plaintext,fichier_key,binaire): #Chiffrement du fichier
    if binaire != 0:
        with open(fichier_plaintext,'rb') as f:#Recup du plaintext
            plaintext = StringToList(f.read())       
    else:
        with open(fichier_plaintext,'r',encoding = 'utf-8') as f:#Recup du plaintext
            plaintext = StringToList(f.read())
    key=[]
    n=0
    with open(fichier_key,'r',encoding = 'utf-8') as f:#Recup de la clé
        key_string = StringToList(f.read())
        for val in key_string:
            if val == ' ':
                key.append(n)
                n=0
            else:
                n*=10
                n+=int(val)
        key.append(n) #Ajout du dernier nombre
    if len(key) != 16:
        return -1
    ciphertext=envoi_crypto(plaintext,key)
    with open('chiffrement.csv', 'w',newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        cipher_string=map(str,ciphertext)
        spamwriter.writerow(cipher_string)
    return 0
        
def lecture_plaintext(fichier_ciphertext,fichier_save,fichier_key,binaire): #Déchiffrement du fichier
    key=[]
    n=0
    with open(fichier_key,'r',encoding = 'utf-8') as f:#Recup de la clé
        key_string = StringToList(f.read())
        for val in key_string:
            if val == ' ':
                key.append(n)
                n=0
            else:
                n*=10
                n+=int(val)
        key.append(n) #Ajout du dernier nombre
    if len(key) != 16:
        return -1
    with open(fichier_ciphertext, 'r',newline='') as csvfile:
        ciphertext = csv.reader(csvfile)
        for d in ciphertext:
            data = list(map(int,d))
    plaintext_data = recoi_decrypt(data,key)
    if binaire != 0:
        with open(fichier_save, 'wb') as f:
            f.write(bytearray(plaintext_data))
    else:
        with open(fichier_save, 'w') as f:
            for carac in plaintext_data:
                if carac != 0:
                    f.write(chr(carac))


   
           
