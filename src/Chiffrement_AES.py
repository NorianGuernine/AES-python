import numpy as np
from CF_Multi import CF_Mult2, CF_Mult3
from Operation_cle import AddRoundKey, KeyExpansion
from MiseEnForme import *
from Matrices import Sbox, Rcon
        
def SubBytes(state,Sbox):   #Subbyte pour AES
    for i in range(0,state.shape[0]):
        for n in range(0,state.shape[1]):
            state[i][n]=Sbox[( state[i][n]&0xF0)>>4,state[i][n]&0x0F]
    return state

def ShiftRows(state):   #ShiftRows pour AES
    state=state
    for i in range(0,state.shape[1]):
        state[i]=np.roll(state[i],-i)
    return state  

def MixColumns(state):  #MixColums pour AES
    state=state.T
    for i in range(0,state.shape[1]):
        a=tuple(state[i])
        state[i][0]=CF_Mult2(a[0]) ^ CF_Mult3(a[1]) ^ a[2] ^ a[3]
        state[i][1]=a[0] ^ CF_Mult2(a[1]) ^ CF_Mult3(a[2]) ^ a[3] 
        state[i][2]=a[0] ^ a[1] ^ CF_Mult2(a[2]) ^ CF_Mult3(a[3])
        state[i][3]=CF_Mult3(a[0]) ^ a[1] ^ a[2] ^ CF_Mult2(a[3])
    return state.T

def Rijndael(plaintext,key):    #Chiffrement
    state=AddRoundKey(plaintext,key[0])
    for i in range(1,10):
        state=SubBytes(state,Sbox)
        state=ShiftRows(state)
        state=MixColumns(state)
        state=AddRoundKey(state,key[i])
    state=SubBytes(state,Sbox)
    state=ShiftRows(state)
    state=AddRoundKey(state,key[10])
    return state

def envoi_crypto(plaintext,key): #/!\Ne doit recevoir en plaintext que  liste
    cypher=[]
    tampon=[]
    liste=[]
    key=StringToList(key)
    key=MiseEnForme(key)    #Mise de la clé sous forme de matrice 
    keyexpansion=KeyExpansion(key,Sbox) #Generation des clés pour chaque round
    while len(plaintext)>=16:
        tampon=plaintext[0:16]
        tampon=MiseEnForme(tampon)
        cyphertext=Rijndael(tampon,keyexpansion)
        cypher.append(cyphertext)
        for i in range(0,16):
            del plaintext[0]
    if len(plaintext) > 0:
        while(len(plaintext) < 16):
            if type(plaintext[0]) is int:
                plaintext.append(0)
            elif type(plaintext[0]) is str:
                plaintext.append('\0')
            else:
                return -1
        plaintext=MiseEnForme(plaintext)
        cyphertext=Rijndael(plaintext,keyexpansion)
        cypher.append(cyphertext)
    for array in cypher: #Conversion de la matrice en liste 1 dimension
        for element in array: #Conversion de la matrice en liste 1 dimension
            for element2 in element:
                liste.append(element2)
    return liste #Retourne liste chiffré

