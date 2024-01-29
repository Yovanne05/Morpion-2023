# Créé par YovannePONNOU, le 11/01/2022 en Python 3.7
from tkinter import *

fenetre = Tk()
fenetre.title("Morpion")

Largeur = 300
Hauteur = 300
morpion = Canvas(fenetre, width = Largeur, height =Hauteur, background ="white")
#Création d'un carré
morpion.pack(padx =10, pady =10)
#Création des cases
morpion.create_line(0,100,300,100,fill="black")

morpion.create_line(0,200,300,200,fill="black")

morpion.create_line(100,300,300,-200000,fill="black")

morpion.create_line(200,300,300,-100000,fill="black")

#def reinit():


# Bouton Quitter
bouton = Button(fenetre,text='Quitter',command=fenetre.destroy).pack(side=RIGHT)
#bouton2 =Button(fenetre,text='Recommencer',command=reinit).pack(side=LEFT)

fenetre.mainloop()

#Fonction pour créé des ronds
def rond():
    Canevas.create_oval(x1-50,y1-50,x1+50,y1+50)

fenetre.mainloop()


#Fontion pour créé des croix
def croix():
    Canvas.create_text("X")
