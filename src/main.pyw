from tkinter import *
import tkinter.filedialog
from tkinter.messagebox import *
from crypt_decrypt_fichier import *

def Ouverture_fichier_cle():
    try:
        filename = tkinter.filedialog.askopenfilename(title="Ouvrir fichier clé",filetypes=[('text files','.txt'),('all files','.*')])
        path_key.set(filename)
        with open(filename,'r',encoding = 'utf-8') as f:
            val_key.set(f.read())
    except FileNotFoundError:
        pass

def Ouverture_fichier_plaintext():
    filename = tkinter.filedialog.askopenfilename(title="Ouvrir fichier plaintext",filetypes=[('all files','.*')])
    path_plaintext.set(filename)
    
def Chiffrement_plaintext():
    filetosave=tkinter.filedialog.asksaveasfile(title="Enregistrer fichier",filetypes=[('All Files', '*.*')])
    try:
        chiffrement = ecriture_ciphertext(path_plaintext.get(),path_key.get(),filetosave.name)
        if chiffrement == -1:
            showwarning("Erreur","La taille de la clé n'est pas bonne")
    except FileNotFoundError:
        showwarning("Erreur","Il semble qu'il manque un fichier")

def Ouvrir_fichier_cipher():
    filename = tkinter.filedialog.askopenfilename(title="Ouvrir fichier cipher",filetypes=[('all files','.*')])
    path_ciphertext.set(filename)
    
def dechiffrement_plaintext():
    filetosave=tkinter.filedialog.asksaveasfile(title="Enregistrer fichier",filetypes=[('All Files', '*.*')])
    try:
        dechiffrement = lecture_plaintext(path_ciphertext.get(),filetosave.name,path_key.get())
        if dechiffrement == -1:
            showwarning("Erreur","La taille de la clé n'est pas bonne")
    except FileNotFoundError:
        showwarning("Erreur","Il semble qu'il manque un fichier")
 

    
# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Chiffrement et déchiffrement")

#Init variables
fichier_binaire = IntVar()
fichier_binaire2 = IntVar()
path_plaintext= StringVar()
path_ciphertext= StringVar()

# création d'un widget Frame pour cle dans la fenêtre principale 
Frame1 = Frame(fenetre,width=500, height=500, borderwidth=2,relief=GROOVE)
Frame1.pack(side=TOP,padx=20,pady=20)

# Création d'un widget Label (texte 'clé de chiffrement')
Label_cle = Label(Frame1, text = 'Clé de chiffrement')
Label_cle.grid(columnspan = 4)

# Création d'un widget Entry (chemin de la clé)
path_key= StringVar()
Champ = Entry(Frame1,textvariable= path_key,width = 50)
Champ.focus_set()
Champ.grid(row=1,column=0,padx =0, pady =10)

# Création d'un widget Button (bouton Ouvrir fichier cle.txt)
Ouvrir_cle = Button(Frame1, text ='Ouvrir', command = Ouverture_fichier_cle)
Ouvrir_cle.grid(row=1,column=1,padx =0, pady =10)

# Création d'un widget Label (texte 'clé de chiffrement')
Label_cle = Label(Frame1, text = 'Valeur de la clé (hexadécimal)')
Label_cle.grid(columnspan = 4)

# Création d'un widget Entry (valeure de la clé)
val_key= StringVar()
Champ2 = Entry(Frame1, textvariable= val_key,width = 50)
Champ2.focus_set()
Champ2.grid(row=3,column=0,padx =0, pady =10)

# création d'un widget Frame pour chiffrement dans la fenêtre principale 
Frame2 = Frame(fenetre,width=500, height=500, borderwidth=2,relief=GROOVE)
Frame2.pack(side=TOP,padx=20,pady=20)

# Création d'un widget Label (texte 'plaintext')
Label_plaintext = Label(Frame2, text = 'Chiffrement')
Label_plaintext.grid(columnspan = 4)

# Création d'un widget Entry (chemin du plaintext)
Champ_plaintext = Entry(Frame2, textvariable= path_plaintext,width = 50)
Champ_plaintext.focus_set()
Champ_plaintext.grid(row=2,column=0,padx =0, pady =10)

# Création d'un widget Button (bouton Ouvrir fichier plaintext)
Ouvrir_plaintext = Button(Frame2, text ='Ouvrir', command = Ouverture_fichier_plaintext)
Ouvrir_plaintext.grid(row=2,column=1,padx =0, pady =10)

# Création d'un widget Button (bouton Chiffrer fichier plaintext)
Ouvrir_plaintext = Button(Frame2, text ='Chiffrer', command = Chiffrement_plaintext)
Ouvrir_plaintext.grid(row=3,columnspan = 4,padx =0, pady =5)

# création d'un widget Frame pour déchiffrement dans la fenêtre principale 
Frame3 = Frame(fenetre,width=500, height=500, borderwidth=2,relief=GROOVE)
Frame3.pack(side=TOP,padx=20,pady=20)

# Création d'un widget Label (texte 'plaintext')
Label_ciphertext = Label(Frame3, text = 'Déchiffrement')
Label_ciphertext.grid(columnspan = 4)

# Création d'un widget Entry (chemin du ciphertext)
Champ_ciphertext = Entry(Frame3, textvariable= path_ciphertext,width = 50)
Champ_ciphertext.focus_set()
Champ_ciphertext.grid(row=2,column=0,padx =0, pady =10)

# Création d'un widget Button (bouton Ouvrir fichier ciphertext)
Ouvrir_ciphertext = Button(Frame3, text ='Ouvrir', command = Ouvrir_fichier_cipher)
Ouvrir_ciphertext.grid(row=2,column=1,padx =0, pady =10)

# Création d'un widget Button (bouton Chiffrer fichier plaintext)
Ouvrir_plaintext = Button(Frame3, text ='Déchiffrer', command = dechiffrement_plaintext)
Ouvrir_plaintext.grid(row=3,columnspan = 4,padx =0, pady =5)


#Montage fenêtre
fenetre.mainloop()
