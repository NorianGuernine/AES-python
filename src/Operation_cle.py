import numpy as np
from Matrices import Rcon

def AddRoundKey(state,key): #Roundkey pour AES
    for i in range(0,state.shape[0]):
        state[i]=state[i]^key[i]
    return state

def KeySchedule(key,cycle,tab): #KeySchedule pour chiffrement et déchiffrement AES
    key=key.T
    key2=np.array(key)
    key2[0]=np.roll(key[3],-1)
    for i in range(0,key2.shape[1]):
        key2[0][i]=tab[(key2[0][i]&0xF0)>>4,key2[0][i]&0x0F]
    key2[0]=key2[0] ^ key[0] ^ Rcon.T[cycle]
    for i in range(1,key.shape[1]):
        key2[i]=key[i] ^ key2[i-1]
    return key2.T

def KeyExpansion(key,tab):  #Calcul des clés de chiffrement pour tous les rounds en même temps
    keyexpansion=[key]
    for i in range(0,10):
        keyexpansion.append(KeySchedule(keyexpansion[i],i,tab))
    return keyexpansion
