# Créé par YovannePONNOU, le 11/01/2022 en Python 3.7
#module
from tkinter import *
from PIL import ImageTk, Image

#image
croix = PhotoImage(file ='croix.png')


#fenetre
fenetre = Tk()
fenetre.title("Morpion")

def jouer():
    lab1.configure(image=croix)

#bouton
bouton1 = Button(fenetre, command=jouer)
bouton1.configure(image=rien)
bouton1.grid(row=1, column=0)


#démarage
fenetre.mainloop()
