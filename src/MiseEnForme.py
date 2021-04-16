import numpy as np

def StringToList(string): #Conversion de l'entrée en liste si il s'agit d'une chaine de caractère
    list1=[] 
    list1[:0]=string 
    return list1

def MiseEnForme(string): #Mise de l'entrée sous forme de matrice recoit en entrée chaine de caractère ou liste de type int ou bytes 
    if type(string[0]) is str:
        for i in range(0,16):
            string[i]=ord(string[i])
    list1=np.array(string).reshape(-1,4).astype(np.uint8)
    return list1
