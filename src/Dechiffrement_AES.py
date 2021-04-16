import numpy as np
from CF_Multi import CF_Mult9, CF_Mult11, CF_Mult13, CF_Mult14
from Operation_cle import AddRoundKey, KeyExpansion
from MiseEnForme import *
from Matrices import InvSbox, Sbox, Rcon


def InvSubBytes(state,InvSbox): #Inversion du Subbytes pour déchiffrement AES
    for i in range(0,state.shape[0]):
        for n in range(0,state.shape[1]):
            state[i][n]=InvSbox[(state[i][n]&0xF0)>>4,state[i][n]&0x0F]
    return state

def InvShiftRows(state):    #Inversion du ShiftRows pour déchiffrement AES
    state=state
    for i in range(0,state.shape[1]):
        state[i]=np.roll(state[i],i)
    return state    


def InvMixColumns(state):   #Inversion du MixColums pour déchiffrement AES
    state=state.T
    for i in range(0,state.shape[1]):
        a=tuple(state[i])
        state[i][0]=CF_Mult14(a[0]) ^ CF_Mult11(a[1]) ^ CF_Mult13(a[2]) ^ CF_Mult9(a[3])
        state[i][1]=CF_Mult9(a[0]) ^ CF_Mult14(a[1]) ^ CF_Mult11(a[2]) ^ CF_Mult13(a[3]) 
        state[i][2]=CF_Mult13(a[0]) ^ CF_Mult9(a[1]) ^ CF_Mult14(a[2]) ^ CF_Mult11(a[3])
        state[i][3]=CF_Mult11(a[0]) ^ CF_Mult13(a[1]) ^ CF_Mult9(a[2]) ^ CF_Mult14(a[3])
    return state.T


def InvRijndael(ciphertext,key):
    state=AddRoundKey(ciphertext,key[10])
    state=InvShiftRows(state)
    state=InvSubBytes(state,InvSbox)
    for i in range(9,0,-1):
        state=AddRoundKey(state,key[i])
        state=InvMixColumns(state)
        state=InvShiftRows(state)
        state=InvSubBytes(state,InvSbox)
    state=AddRoundKey(state,key[0])
    return state

def recoi_decrypt(ciphertext,key): #/!\Ne doit recevoir en plaintext que  liste
    plain=[]
    tampon=[]
    liste=[]
    key=StringToList(key)
    key=MiseEnForme(key)    #Mise sous la forme de matrice de la clé
    keyexpansion=KeyExpansion(key,Sbox) #Generation des clés pour chaque round
    while len(ciphertext)>16:
        tampon=ciphertext[0:16]
        tampon=MiseEnForme(tampon)
        plaintext=InvRijndael(tampon,keyexpansion)
        plain.append(plaintext)
        for i in range(0,16):
            del ciphertext[0]
    if len(ciphertext) > 0:
        while(len(ciphertext) < 16):
            if type(ciphertext[0]) is int:
                ciphertext.append(0)
            elif type(ciphertext[0]) is str:
                ciphertext.append('\0')
            else:
                return -1
        ciphertext=MiseEnForme(ciphertext)
        plaintext=InvRijndael(ciphertext,keyexpansion)
        plain.append(plaintext)
    for array in plain: #Conversion de la matrice en liste 1 dimension
        for element in array: #Conversion de la matrice en liste 1 dimension
            for element2 in element:
                liste.append(element2)
    return liste #Retourne liste chiffré

