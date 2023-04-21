"""Fait par Yohann, Dimitri, Amine et Aboubakr"""
import tkinter as tk
from random import *
import numpy as np # libraire pour effectuer des probabilités sur les tuiles
import couleurs2048 as color # librairie pour les couleurs des tuiles/canvas
import pickle as pc # librairie pour la sauvegarde et le chargement de parties

## Création de la fenêtre graphique :

root = tk.Tk()
root.title("2048")

## Variables globales principales qu'on appellera dans plusieurs fonctions :

cases = []   # possède les détail de chaque tuile

grille = [] # possède les nombres présents sur la grille  

##  FONCTIONS CONCERNANT L'INTERFACE GRAPHIQUE :

# Fonction qui va créer l'interface graphique du jeu 2048 :   

def Plateforme():
    global cases
    for i in range (4):
        rangée = []
        for j in range (4):
            frame = tk.Frame(bg_grille, bg="#c2b3a9" , width=120, height=120)
            frame.grid(row=i, column=j, padx=5, pady=5)
            nombre = tk.Label(bg_grille, bg="#c2b3a9" )
            nombre.grid(row=i, column=j)
            case_dict = {"cases": frame, "nombre": nombre}
            rangée.append(case_dict)
        cases.append(rangée)
    

# La fonction suivante sert à mettre à jour la plateforme de jeu (modifier les affichages des cases) :

def Maj_Plateforme():
    global cases
    for i in range (4):
        for j in range (4):
            if grille[i][j] == 0:
                cases[i][j]["cases"].config(bg="#c2b3a9" )
                cases[i][j]["nombre"].config(bg="#c2b3a9" , text="") 
            else:
                cases[i][j]["cases"].config(bg=color.Couleurs_cases[grille[i][j]])
                cases[i][j]["nombre"].config(bg=color.Couleurs_cases[grille[i][j]],fg=color.Couleurs_nombres[grille[i][j]],font=color.Fonts[grille[i][j]], text=str(grille[i][j]))
    

##  FONCTIONS CONCERNANT LA FIN D'UNE PARTIE :

score = None   # variable qui nous donnera le résultat de la partie, elle prendra 0 si elle est perdue

## La fonction suivante transmet Loose() si le joueur a perdu :

def Fin_partie():
    global score
    if Vide_mat() == False and Test_horizontale() == False and Test_Verticale() == False : 
        score = 0
        Lose()

## Fonction qui affiche "Perdu!" si on a perdu :

loose = tk.Label()

def Lose():
    global loose
    Plateforme()
    Maj_Plateforme()
    if score==0:
        affichage_end = tk.Frame(bg_grille, borderwidth=4)
        affichage_end.place(relx=0.5, rely=0.5, anchor="center")
        loose = tk.Label(affichage_end,  text="Perdu!", bg="#e64c2e", fg="#ffffff", font=("Arial", 50,"bold")).pack()


##  FONCTIONS PERMETTANT DE FAIRE DES TESTS PENDANT LA PARTIE (pour savoir quand la partie est perdu) :

## Fonction qui permet de vérifier si il y a encore des cases vides dans la grille du jeu, pour vérifier s'il est possible de générer une nouvelle tuile sur la grille :

def Vide_mat():
    for i in range(4):
        if 0 in grille[i]:
            return True
    return False

## Fonction qui détermine si un mouvement est possible dans une direction verticale :


def Test_Verticale():
    for i in range (1,3):
        for j in range (4):
            if grille[i][j] == grille[i+1][j] or grille[i][j] == grille[i-1][j]:
                return True
    return False

## Fonction qui détermine si un mouvement est possible dans une direction horizontale :

def Test_horizontale():
    for i in range (4):
        for j in range (1,3):
            if grille[i][j] == grille[i][j+1] or grille[i][j] == grille[i][j-1]:
                return True
    return False


## FONCTIONS AUX DIFFRENTS BOUTONS : 

## Fonction utilisé pour le début d'une partie (on l'appellera pour la fonction du bouton Start),
# elle permet de commencer le jeu en plaçant aléatoirement 2 tuiles de valeurs 2 ou 4 :

def Debut_Partie():
    global grille, cases
    grille = []
    cases = []
    Plateforme()
    grille = [[0]*4 for _ in range (4)]
    i = randint(0,3)
    j = randint(0,3)
    grille[i][j] = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1]) 
    cases[i][j]["cases"].config(bg=color.Couleurs_cases[grille[i][j]])
    cases[i][j]["nombre"].config(bg=color.Couleurs_cases[grille[i][j]], text=str(grille[i][j]), fg=color.Couleurs_nombres[grille[i][j]], font=color.Fonts[grille[i][j]])
    while grille[i][j]!=0:
        i = randint(0,3)
        j = randint(0,3)
    grille[i][j] = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1]) 
    cases[i][j]["cases"].config(bg=color.Couleurs_cases[grille[i][j]])
    cases[i][j]["nombre"].config(bg=color.Couleurs_cases[grille[i][j]], text=str(grille[i][j]), fg=color.Couleurs_nombres[grille[i][j]], font=color.Fonts[grille[i][j]])

## Les fonctions ci-dessous permettent de concaténer deux tuiles de la même valeur dans la direction mentionée : 

def Concatener_Up(matrice):
    for i in range (3):
        for j in range (4):
            if matrice[i][j] != 0 and matrice[i][j] == matrice[i+1][j] :
                matrice[i][j] *= 2
                matrice[i+1][j] = 0
    return matrice

def Concatener_Down(matrice):
    for i in range (1,4):
        for j in range (4):
            if matrice[-i][j] != 0 and matrice[-i][j] == matrice[-i-1][j] :
                matrice[-i][j] *= 2
                matrice[-i-1][j] = 0
    return matrice

def Concatener_Left(matrice):
    for i in range (4):
        for j in range (3):
            if matrice[i][j] != 0 and matrice[i][j] == matrice[i][j+1]:
                matrice[i][j] *= 2
                matrice[i][j+1] = 0
    return matrice
                
def Concatener_Right(matrice):
    for i in range (4):
        for j in range (1,4):
            if matrice[i][-j] != 0 and matrice[i][-j] == matrice[i][-j-1] :
                matrice[i][-j] *= 2
                matrice[i][-j-1] = 0
    return matrice

## Les fonctions qui superposent les tuiles les unes sur les autres, elles déplacent les tuiles non-nulles de la grille vers la direction mentionée :

def Superposer_Up(matrice):
    new_matrice = [[0]*4 for i in range(4)]
    for j in range (4):
        position = 0
        for i in range (4):
            if matrice[i][j] != 0:
                new_matrice[position][j] = matrice[i][j]
                position+=1
    matrice = new_matrice
    return matrice

def Superposer_Down(matrice):
    new_matrice = [[0]*4 for i in range(4)]
    for j in range (4):
        position = -1
        for i in range (1,5):
            if matrice[-i][j] != 0:
                new_matrice[position][j] = matrice[-i][j]
                position-=1
    matrice = new_matrice
    return matrice

def Superposer_Left(matrice):
    new_matrice = [[0]*4 for i in range(4)]
    for i in range (4):
        position = 0
        for j in range (4):
            if matrice[i][j] != 0:
                new_matrice[i][position] = matrice[i][j]
                position+=1
    matrice = new_matrice  
    return matrice
    
def Superposer_Right(matrice):
    new_matrice = [[0]*4 for i in range(4)]
    for i in range (4):
        position = -1
        for j in range (1,5):
            if matrice[i][-j] != 0:
                new_matrice[i][position] = matrice[i][-j]
                position-=1
    matrice = new_matrice
    return matrice


## Fonction qui créera à chaque déplacement une tuile aléatoire dans la grille (s'il y a des cases vides) :

def tuile_aleatoire(matrice):
    ligne = randint(0,3)
    colonne = randint(0,3)
    if Vide_mat() == True:
        while matrice[ligne][colonne]!=0:
            ligne = randint(0,3)
            colonne = randint(0,3)
        matrice[ligne][colonne] = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    return matrice

 # Fonction pour le bouton "Save" :
def save_button():
    fichier = open("sauvegarde-2048.txt", "wb") 
    pc.dump(grille, fichier)
    fichier.close()

 # Fonction pour le bouton "Load" :
def load_button():
    global grille
    matrice = []
    fichier = open("sauvegarde-2048.txt", "rb")
    fichier_ouvert = pc.load(fichier)
    fichier.close()
    for l in fichier_ouvert:
        matrice.append(l)
    grille = matrice
    Maj_Plateforme()

 # Fonction pour le bouton "Start" :
def start_button():
    Debut_Partie()

 # Fonction pour le bouton "Exit"  :     
def exit_button():
    root.destroy()

  # Fonction pour le bouton "Up" :
def up_button():
    global grille
    grille = Superposer_Up(grille)
    grille = Concatener_Up(grille)
    grille = Superposer_Up(grille)
    grille = tuile_aleatoire(grille)
    Maj_Plateforme()
    Fin_partie()

  # Fonction pour le bouton "Down" :
def down_button():
    global grille
    grille = Superposer_Down(grille)
    grille = Concatener_Down(grille)
    grille = Superposer_Down(grille)
    grille = tuile_aleatoire(grille)
    Maj_Plateforme()
    Fin_partie()

  # Fonction pour le bouton "Left" :
def left_button():
    global grille
    grille = Superposer_Left(grille)
    grille = Concatener_Left(grille)
    grille = Superposer_Left(grille)
    grille = tuile_aleatoire(grille)
    Maj_Plateforme()
    Fin_partie()

  # Fonction pour le bouton "Right" :
def right_button():
    global grille
    grille = Superposer_Right(grille)
    grille = Concatener_Right(grille)
    grille = Superposer_Right(grille)
    grille = tuile_aleatoire(grille)
    Maj_Plateforme()
    Fin_partie()

# Couleur de fond de la grile :
        
bg_grille = tk.Frame(root,width=570, height=570, bg="#a39489", bd=5) 
bg_grille.grid(pady=20,row=0,column=0,rowspan=20,padx=20)

## Boutons principales :

Save = tk.Button(text="Save", font=("Helvetica", "12","bold"),bg="#f5b682",height=1, width=4,command=save_button)
Save.grid(row=8, column=2)

Load = tk.Button(text="Load",font=("Helvetica", "12","bold"),bg='#f5b682',height=1, width=4,command=load_button)
Load.grid(row=9, column=2)

Start = tk.Button(text="Start",font=("Helvetica", "12","bold"),bg="#fce130",height=1, width=4,command=start_button)
Start.grid(row=2, column=2)

Exit = tk.Button(text="Exit",font=("Helvetica", "12","bold"),bg="#ff775c",height=1, width=4,command=exit_button)
Exit.grid(row=3, column=2)


# Boutons pour se déplacer dans le jeu :

# Haut :
    
Up = tk.Button(text="Up",font=("Helvetica", "12","bold"), bg="#f2e8cb",height=1, width=5, command=up_button)
Up.grid(row=14, column=2)

# Bas :

Down = tk.Button(text="Down", font=("Helvetica", "12","bold"), bg="#f2e8cb", height=1, width=5,command=down_button)
Down.grid(row=16, column=2)

# Gauche :

Left = tk.Button(text="Left", font=("Helvetica", "12","bold"), bg="#f2e8cb",height=1, width=5,command=left_button)
Left.grid(row=15, column=1)

# Droite :

Right = tk.Button(text="Right",font=("Helvetica", "12","bold"), bg="#f2e8cb",height=1, width=5,command=right_button)
Right.grid(row=15, column=3,padx=8)


Plateforme()

root.mainloop()