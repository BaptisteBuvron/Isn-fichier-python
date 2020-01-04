#Import
import time
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os

#Init
ascii = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Alphabet
path_read_file = "germinal01.txt"
path_save_file = "germinal_number.txt"
response = {} #Dictionaries
debut = time.time()
number = int
erreur = False
total = 0
texte =""


def read_line():
    global texte
    fichier_texte=open(path_read_file,'r')
    texte=fichier_texte.readlines()
    fichier_texte.close()

def calcul_lettre():
    global texte
    global response
    global number
    i= 0
    for i in range(len(ascii)):
        texte = str(texte)
        number = texte.count(str(ascii[i]))
        response[ascii[i]] = number

def write_tkinter():
    global path_read_file
    global response
    total = 0
    i=2
    ma_fenetre.Titre=Label(ma_fenetre,text="Analyse de : " +os.path.basename(path_read_file))
    ma_fenetre.Titre.grid(row=0,column=5)
    for letter, number in response.items():
        phrase = "Nombre de  "+str(letter)+" = "+str(number)
        label_response =Label(ma_fenetre, text=phrase)
        label_response.grid(row=i,column=5)
        i+=1
    bouton_quitter.grid(row=i+1,column=8)
    ma_fenetre.button_save_location.grid(row=3, column=0)
    ma_fenetre.button_save.grid(row=5, column=0)


def write_file():
    global total
    global path_read_file
    global path_save_file
    global response
    global debut
    global erreur
    if erreur == False:
        file_text=open(path_save_file,'w')
        file_text.write("Analyse de : " +os.path.basename(path_read_file) +"\n\n")
        for letter, number in response.items():
	        phrase = "Nombre de  "+str(letter)+" = "+str(number)
	        total+=int(number)
	        file_text.write(phrase+"\n")
        file_text.write("\n"+"Il y a : "+str(total)+" lettres.")
        fin = time.time()
        file_text.write("\n"+"Analyse effectuee en "+str(fin-debut)+" secondes.")
        file_text.close()

	
def file_select():
    global path_read_file
    path_read_file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
    if os.path.exists(path_read_file) == False:
        ma_fenetre.path.config(text=" erreur")
        erreur = True
    else:
        ma_fenetre.path.config(text=path_read_file)
        erreur = False
        
def file_save():
    global path_save_file
    path_save_file = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))

def text_changed():
    global ascii
    ascii = str(ma_fenetre.ascii.get())




def main():
    if erreur == False:
        read_line()
        calcul_lettre()
        write_tkinter()





########################### 
#   Programme principal   #
########################### 


ma_fenetre=Tk()
ma_fenetre.title("calcul lettre")

ma_fenetre.label_a=Label(ma_fenetre,text="Choisir le fichier a étudier")
ma_fenetre.label_a.grid(row=0,column=0)

ma_fenetre.button_file_select = Button(ma_fenetre, text="Choisir un fichier", command =file_select)
ma_fenetre.button_file_select.grid(row=0, column=1)

ma_fenetre.path=Label(ma_fenetre,text=path_read_file)
ma_fenetre.path.grid(row=0,column=2)

ma_fenetre.ascii= Label(ma_fenetre, text="Définir votre alphabet : ")
ma_fenetre.ascii.grid(row=1,column=0)

sv =StringVar()
ma_fenetre.ascii=Entry(ma_fenetre,textvariable = sv, validate="focusout", validatecommand=text_changed)
ma_fenetre.ascii.insert(END,ascii)
ma_fenetre.ascii.grid(row=1,column=1)

ma_fenetre.button_start = Button(ma_fenetre, text="Calcul", command =main)
ma_fenetre.button_start.grid(row=3, column=1)

bouton_quitter = Button(ma_fenetre, text ='Quitter', command = ma_fenetre.destroy)
bouton_quitter.grid(row=5,column=3)

ma_fenetre.button_save = Button(ma_fenetre, text="Save", command =write_file)
ma_fenetre.button_save_location = Button(ma_fenetre, text="Choisir le fichier de la sauvegarde ", command =file_save)


ma_fenetre.mainloop()




