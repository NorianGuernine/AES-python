#Test cryptage des messages avec taille variable
import numpy as np
from MiseEnForme import MiseEnForme
from Operation_cle import KeyExpansion
from Chiffrement_AES import *
from Dechiffrement_AES import *
from Matrices import Sbox, Rcon

#Cle de chiffrement 
key=b'\x2b\x28\xAB\x09\x7E\xAE\xF7\xCF\x15\xD2\x15\x4F\x16\xA6\x88\x3C'
#key=MiseEnForme(key)    #Mise sous la forme de matrice de la clé
#keyexpansion=KeyExpansion(key,Sbox) #Generation des clés pour chaque round

#Message a chiffrer n°1 (moins de 16 caracères)
plaintext1="Message secret"
plaintext1 = StringToList(plaintext1)
cr1=envoi_crypto(plaintext1,key)
#print("Ciphertext (decimal)= "+str(cr1)+ "\n")
#Message n°1 Déchiffré
d=recoi_decrypt(cr1,key)
#print("plaintext dechiffrer (decimal)= "+str(d)+ "\n")

