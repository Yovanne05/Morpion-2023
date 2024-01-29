#module
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

#Titre
fenetre = Tk()
fenetre.title("Morpion")

titre=Label(fenetre, text="Morpion", font=('Arial', 12))
titre.grid(row=0, column=1)

compteur=0

liste=[" ", " ", " ", " ", " ", " ", " ", " ", " "]


#Fonctionnement du morpion
def jouer1():
    global compteur
    if  compteur % 2 == 0:
        bouton1.configure(text="X")
        liste[0]="X"
    else:
        bouton1.configure(text="0")
        liste[0]="O"

    compteur +=1

    bouton1.configure(state=DISABLED)
    gagnant(liste)


def jouer2():
    global compteur
    if  compteur % 2 == 0:
        bouton2.configure(text="X")
        liste[1]="X"
    else:
        bouton2.configure(text="0")
        liste[1]="O"
    compteur +=1
    bouton2.configure(state=DISABLED)
    gagnant(liste)


def jouer3():
    global compteur
    if compteur % 2 == 0:
        bouton3.configure(text="X")
        liste[2]="X"
    else:
        bouton3.configure(text="0")
        liste[2]="O"
    compteur +=1

    bouton3.configure(state=DISABLED)
    gagnant(liste)

def jouer4():
    global compteur
    if compteur % 2 == 0:
        bouton4.configure(text="X")
        liste[3]="X"
    else:
        bouton4.configure(text="0")
        liste[3]="O"
    compteur +=1

    bouton4.configure(state=DISABLED)
    gagnant(liste)

def jouer5():
    global compteur
    if compteur % 2 == 0:
        bouton5.configure(text="X")
        liste[4]="X"
    else:
        bouton5.configure(text="0")
        liste[4]="O"
    compteur +=1

    bouton5.configure(state=DISABLED)
    gagnant(liste)

def jouer6():
    global compteur
    if compteur % 2 == 0:
        bouton6.configure(text="X")
        liste[5]="X"
    else:
        bouton6.configure(text="0")
        liste[5]="O"
    compteur +=1

    bouton6.configure(state=DISABLED)
    gagnant(liste)

def jouer7():
    global compteur
    if compteur % 2 == 0:
        bouton7.configure(text="X")
        liste[6]="X"
    else:
        bouton7.configure(text="0")
        liste[6]="O"
    compteur +=1
    bouton7.configure(state=DISABLED)
    gagnant(liste)

def jouer8():
    global compteur
    if compteur % 2 == 0:
        bouton8.configure(text="X")
        liste[7]="X"
    else:
        bouton8.configure(text="0")
        liste[7]="O"
    compteur +=1

    bouton8.configure(state=DISABLED)
    gagnant(liste)

def jouer9():
    global compteur
    if compteur %2 == 0:
        bouton9.configure(text="X")
        liste[8]="X"
    else:
        bouton9.configure(text="0")
        liste[8]="O"
    compteur +=1

    bouton9.configure(state=DISABLED)
    gagnant(liste)

def gagnant(liste):
    global compteur
    vainqueur = False
    #(0,1,2);(3,4,5);(6,7,8);(0,4,8);(2,4,6);(0,3,6);(1,4,7);(2,5,8)
    if (liste[0] == "O" and liste[1] == "O" and liste[2] == "O") or (liste[0] == "X" and liste[1] == "X" and liste[2] == "X"):
        vainqueur = True
        blocage()
    elif (liste[3] == "O" and liste[4] == "O" and liste[5] == "O") or (liste[3] == "X" and liste[4] == "X" and liste[5] == "X"):
        vainqueur = True
        blocage()
    elif (liste[6] == "O" and liste[7] == "O" and liste[8] == "O") or (liste[6] == "X" and liste[7] == "X" and liste[8] == "X"):
        vainqueur = True
        blocage()
    elif (liste[0] == "O" and liste[4] == "O" and liste[8] == "O") or (liste[0] == "X" and liste[4] == "X" and liste[8] == "X"):
        vainqueur = True
        blocage()
    elif (liste[2] == "O" and liste[4] == "O" and liste[6] == "O") or (liste[2] == "X" and liste[4] == "X" and liste[6] == "X"):
        vainqueur = True
        blocage()
    elif (liste[2] == "O" and liste[5] == "O" and liste[8] == "O") or (liste[2] == "X" and liste[5] == "X" and liste[8] == "X"):
        vainqueur = True
        blocage()
    elif (liste[0] == "O" and liste[3] == "O" and liste[6] == "O") or (liste[0] == "X" and liste[3] == "X" and liste[6] == "X"):
        vainqueur = True
        blocage()
    elif (liste[1] == "O" and liste[4] == "O" and liste[7] == "O") or (liste[1] == "X" and liste[4] == "X" and liste[7] == "X"):
        vainqueur = True
        blocage()

        result = ''
    if True:
        if vainqueur == True:
            if ((compteur-1)%2) == 0:

                result = "Le gagnant est : X "
            else:
                result = "Le gagnant est : O "

        else:
            if compteur%2 == 0:
                result = "Au tour de X"
            else:
                result = "Au tour de O"

        jeuFini = True

        for i in range (len(liste)):
            if(liste[i] == " "):
                jeuFini = False

        if(jeuFini and vainqueur == False):
            result = "Egalité rejouer :)"

    resultatPanel.configure(text=result)
    resultatPanel.grid(row=7, column=1)


def recommencer():
    global compteur
    bouton1.configure(text="")
    bouton1.configure(state=NORMAL)
    bouton2.configure(text="")
    bouton2.configure(state=NORMAL)
    bouton3.configure(text="")
    bouton3.configure(state=NORMAL)
    bouton4.configure(text="")
    bouton4.configure(state=NORMAL)
    bouton5.configure(text="")
    bouton5.configure(state=NORMAL)
    bouton6.configure(text="")
    bouton6.configure(state=NORMAL)
    bouton7.configure(text="")
    bouton7.configure(state=NORMAL)
    bouton8.configure(text="")
    bouton8.configure(state=NORMAL)
    bouton9.configure(text="")
    bouton9.configure(state=NORMAL)
    resultatPanel.configure(text="")

    compteur = 0

    for i in range (len(liste)):
        liste[i] = ' '


def blocage():

    bouton1.configure(state=DISABLED)
    bouton2.configure(state=DISABLED)
    bouton3.configure(state=DISABLED)
    bouton4.configure(state=DISABLED)
    bouton5.configure(state=DISABLED)
    bouton6.configure(state=DISABLED)
    bouton7.configure(state=DISABLED)
    bouton8.configure(state=DISABLED)
    bouton9.configure(state=DISABLED)

#bouton
bouton1 = tk.Button(fenetre, command=jouer1, width=18, height=9)
bouton1.configure(text="")
bouton1.grid(row=1, column=0)
bouton2 = tk.Button(fenetre, command=jouer2, width=18, height=9)
bouton2.configure(text="")
bouton2.grid(row=2, column=0)
bouton3 = tk.Button(fenetre, command=jouer3, width=18, height=9)
bouton3.configure(text="")
bouton3.grid(row=3, column=0)

bouton4 = tk.Button(fenetre, command=jouer4, width=18, height=9)
bouton4.configure(text="")
bouton4.grid(row=1, column=1)
bouton5 = tk.Button(fenetre, command=jouer5, width=18, height=9)
bouton5.configure(text="")
bouton5.grid(row=2, column=1)
bouton6 = tk.Button(fenetre, command=jouer6, width=18, height=9)
bouton6.configure(text="")
bouton6.grid(row=3, column=1)

bouton7 = tk.Button(fenetre, command=jouer7, width=18, height=9)
bouton7.configure(text="")
bouton7.grid(row=1, column=2)
bouton8 = tk.Button(fenetre, command=jouer8, width=18, height=9)
bouton8.configure(text="")
bouton8.grid(row=2, column=2)
bouton9 = tk.Button(fenetre, command=jouer9, width=18, height=9)
bouton9.configure(text="")
bouton9.grid(row=3, column=2)

bouton10 = Button(fenetre,text='Quitter',command=fenetre.destroy)
bouton10.grid(row=4, column=2)

bouton11=Button(fenetre,text='Recommencer',command=recommencer)
bouton11.grid(row=4, column=0)

resultatPanel=Label(fenetre, text="", font=('Arial', 12))
resultatPanel.grid(row=7, column=1)

#démarage
fenetre.mainloop()
