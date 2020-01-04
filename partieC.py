#Import
import time
from tkinter import *
import tkinter as tk

#Init
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Alphabet
fichier_texte=open("germinal01.txt",'r')
texte=fichier_texte.readlines()
fichier_texte.close()
response = {} #Dictionaries
total = 0
debut = time.time()


#Main Program
for i in range(len(ascii_uppercase)):
	texte = str(texte)
	number = texte.count(str(ascii_uppercase[i]))
	response[ascii_uppercase[i]] = number
file_text=open("germinalLetter.txt",'w')
file_text.write("Analyse de Germinal : " + "\n\n")
for letter, number in response.items():
	phrase = "Nombre de  "+str(letter)+" = "+str(number)
	total+=int(number)
	file_text.write(phrase+"\n")
file_text.write("\n"+"Il y a : "+str(total)+" lettres.")
fin = time.time()
file_text.write("\n"+"Analyse effectuee en "+str(fin-debut)+" secondes.")
file_text.close()






