#Import
import time
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os

#Init
ascii = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Alphabet
path_read_file = "germinal01.txt"  #Default Path
path_save_file = "germinal_number.txt"
response = {} #Dictionary
debut = time.time() #Time 
number = int
erreur = False
total = 0
text ="" #Init text from file to ""


def read_line(): #Function that read file from path_read_file 
    global text
    fichier_text=open(path_read_file,'r')
    text=fichier_text.readlines()
    fichier_text.close()

def calcul_lettre(): #Function that calcul letter from text
    global text
    global response
    global number
    i= 0
    for i in range(len(ascii)):
        text = str(text)
        number = text.count(str(ascii[i]))
        response[ascii[i]] = number  #create index name with the letter in the dictionary response

def write_tkinter(): #Function that write response in the tkinter interface
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


def write_file():#Function that write response in a file txt
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

	
def file_select(): #Function that select the path of a file to read it
    global path_read_file
    path_read_file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
    if os.path.exists(path_read_file) == False:
        ma_fenetre.path.config(text=" erreur")
        erreur = True
    else:
        ma_fenetre.path.config(text=path_read_file)
        erreur = False
        
def file_save(): #Function that select the path of a file to save it
    global path_save_file
    path_save_file = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))

def text_changed(): #Function that change the ascii variable
    global ascii
    ascii = str(ma_fenetre.ascii.get())




def main(): #Main function when Calcul is pressed
    if erreur == False:
        read_line()
        text_changed()
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
ma_fenetre.ascii=Entry(ma_fenetre,textvariable = sv, validate="focusout", validatecommand=text_changed)  #When ascii Entry is update call the function text_changed
ma_fenetre.ascii.insert(END,ascii)
ma_fenetre.ascii.grid(row=1,column=1)

ma_fenetre.button_start = Button(ma_fenetre, text="Calcul", command =main) #Call main when button_start is pressed
ma_fenetre.button_start.grid(row=3, column=1)

bouton_quitter = Button(ma_fenetre, text ='Quitter', command = ma_fenetre.destroy)
bouton_quitter.grid(row=5,column=3)

ma_fenetre.button_save = Button(ma_fenetre, text="Save", command =write_file)
ma_fenetre.button_save_location = Button(ma_fenetre, text="Choisir le fichier de la sauvegarde ", command =file_save)


ma_fenetre.mainloop()




