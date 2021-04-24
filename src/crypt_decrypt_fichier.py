# -*- coding: utf-8 -*-
#Chiffrement Dechiffrement fichier

import numpy as np
from MiseEnForme import *
from Operation_cle import KeyExpansion
from Chiffrement_AES import Rijndael, envoi_crypto
from Dechiffrement_AES import InvRijndael, recoi_decrypt
from Matrices import Sbox, Rcon
import csv

def lecture_cle(fichier_key):
    key=[]
    with open(fichier_key,'r',encoding = 'utf-8') as f:#Recup de la clé
        key_string = StringToList(f.read())
    for i in range(0, 32, 2):
        key.append(int("0x"+key_string[i]+key_string[i+1],16))
    if len(key) != 16:
        return -1
    return key
    
def ecriture_ciphertext(fichier_plaintext,fichier_key,chemin_sauvegarde): #Chiffrement du fichier
    with open(fichier_plaintext,'rb') as f:#Recup du plaintext
        plaintext = StringToList(f.read())
    key=lecture_cle(fichier_key)
    if key == -1:
        return -1
    ciphertext=envoi_crypto(plaintext,key)
    with open(chemin_sauvegarde, 'wb') as f:
        f.write(bytearray(ciphertext))
    return 0
        
def lecture_plaintext(fichier_ciphertext,fichier_save,fichier_key): #Déchiffrement du fichier
    n=0
    key=lecture_cle(fichier_key)
    if key == -1:
        return -1
    with open(fichier_ciphertext, 'rb') as f:
        ciphertext = f.read()
    plaintext_data = recoi_decrypt(list(ciphertext),key)
    with open(fichier_save, 'wb') as f:
        f.write(bytearray(plaintext_data))



   
           
