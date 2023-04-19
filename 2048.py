import tkinter as tk # librairie interphace graphique
import random as rd # libraire pour choisir aléatoirement des tuiles
import numpy as np # libraire pour appliquer des probabilités sur les apparitions de tuiles
import couleurs2048 as color # librairie pour les couleurs des tuiles/canvas
import pickle as pc # librairie pour la sauvegarde et le chargement de parties

# Interface graphique
    
root = tk.Tk()
root.title("2048")

# Variables globales :
        
cases = []   # contient chaque détail de chaque tuile (couleur+nombre)
grille = [] # contient les nombres présents sur la grille
score = None   # cette variable donnera si la partie est gagnée ou perdue,
              # 1 = win et 0 = loose


# Fonctions premières  

# Créer l'interface graphique du jeu 2048 : elle prendra    

def Interface():
   #Cette fonction va créer la plateforme de jeu
    global cases
    for i in range (4):
        ligne = []
        for j in range (4):
            case_frame = tk.Frame(background, bg="#c2b3a9" , width=120, height=120)
            case_frame.grid(row=i, column=j, padx=5, pady=5)
            case_nombre = tk.Label(background, bg="#c2b3a9" )
            case_nombre.grid(row=i, column=j)
            case_data = {"frame": case_frame, "number": case_nombre}
            ligne.append(case_data)
        cases.append(ligne)
    
    
def Actualisation_Inter():
    #Cette fonction va actualiser les couleurs/affichages dans le plateau
    global cases
    for i in range (4):
        for j in range (4):
            valeur_case = grille[i][j]
            if valeur_case == 0:
                cases[i][j]["frame"].config(bg="#c2b3a9" )
                cases[i][j]["number"].config(bg="#c2b3a9" , text="") 
            else:
                cases[i][j]["frame"].config(bg=color.COULEURS_CASES[valeur_case])
                cases[i][j]["number"].config(bg=color.COULEURS_CASES[valeur_case],fg=color.COULEURS_NOMBRES[valeur_case],
                                             font=color.FONTS[valeur_case], text=str(valeur_case))

def Generateur_Tuile(mat):
    #Cette fonction donne à matrice une tuile créée aléatoirement
    row = rd.randint(0,3)
    column = rd.randint(0,3)
    if Vide_Mat() == True:
        while mat[row][column]!=0:
            row = rd.randint(0,3)
            column = rd.randint(0,3)
        mat[row][column] = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    else:
        pass
    return mat


    # Empilation
def Empiler_Gauche(mat):
    #Place les tuiles vers la gauche
    matrice2 = [[0]*4 for _ in range (4)]
    for i in range (4):
        pos = 0
        for j in range (4):
            if mat[i][j] != 0:
                matrice2[i][pos] = mat[i][j]
                pos+=1
    mat = matrice2  
    return mat
    
def Empiler_Droite(mat):
    #Place les tuiles vers la droite
    matrice2 = [[0]*4 for _ in range (4)]
    for i in range (4):
        pos = -1
        for j in range (1,5):
            if mat[i][-j] != 0:
                matrice2[i][pos] = mat[i][-j]
                pos-=1
    mat = matrice2
    return mat

def Empiler_Haut(mat):
    #Place les tuiles vers le haut
    matrice2 = [[0]*4 for _ in range (4)]
    for j in range (4):
        pos = 0
        for i in range (4):
            if mat[i][j] != 0:
                matrice2[pos][j] = mat[i][j]
                pos+=1
    mat = matrice2
    return mat

def Empiler_Bas(mat):
    #Place les tuiles vers le bas
    matrice2 = [[0]*4 for _ in range (4)]
    for j in range (4):
        pos = -1
        for i in range (1,5):
            if mat[-i][j] != 0:
                matrice2[pos][j] = mat[-i][j]
                pos-=1
    mat = matrice2
    return mat

# Combinaison
def Combiner_Gauche(mat):
    #Cette fonction permettra de combiner 2 tuiles de même nombre vers la gauche
    for i in range (4):
        for j in range (3):
            if mat[i][j] != 0 and mat[i][j] == mat[i][j+1]:
                mat[i][j] *= 2
                mat[i][j+1] = 0
    return mat
                
def Combiner_Droite(mat):
    #Cette fonction permettra de combiner 2 tuiles de même nombre vers la droit
    for i in range (4):
        for j in range (1,4):
            if mat[i][-j] != 0 and mat[i][-j] == mat[i][-j-1]:
                mat[i][-j] *= 2
                mat[i][-j-1] = 0
    return mat
                
def Combiner_Haut(mat):
    #Cette fonction permettra de combiner 2 tuiles de même nombre vers le haut
    for i in range (3):
        for j in range (4):
            if mat[i][j] != 0 and mat[i][j] == mat[i+1][j]:
                mat[i][j] *= 2
                mat[i+1][j] = 0
    return mat
                
def Combiner_Bas(mat):
    #Cette fonction permettra de combiner 2 tuiles de même nombre vers le bas
    for i in range (1,4):
        for j in range (4):
            if mat[-i][j] != 0 and mat[-i][j] == mat[-i-1][j]:
                mat[-i][j] *= 2
                mat[-i-1][j] = 0
    return mat

## Fonctions associées aux boutons : 

def Generateur():
    #Cette fonction génère 2 tuiles aléatoirement et les affiche dans le jeu
    global cases
    global grille
    # réinitialiser la plateforme de jeu ainsi que les 2 tuiles placées
    grille = []
    cases = []
    Interface()
    
    # début du code
    grille = [[0]*4 for _ in range (4)]
    
    # générer 2 tuiles aléatoires
    row = rd.randint(0,3)
    column = rd.randint(0,3)
    tuile = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    grille[row][column] = tuile 
    cases[row][column]["frame"].config(bg=color.COULEURS_CASES[tuile])
    cases[row][column]["number"].config(bg=color.COULEURS_CASES[tuile], 
                                     fg=color.COULEURS_NOMBRES[tuile], 
                                     font=color.FONTS[tuile], 
                                     text=str(tuile)
                                     )
    while grille[row][column]!=0:
        row = rd.randint(0,3)
        column = rd.randint(0,3)
    tuile = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    grille[row][column] = tuile 
    cases[row][column]["frame"].config(bg=color.COULEURS_CASES[tuile])
    cases[row][column]["number"].config(bg=color.COULEURS_CASES[tuile], 
                                     fg=color.COULEURS_NOMBRES[tuile], 
                                     font=color.FONTS[tuile], 
                                     text=str(tuile)
 
                                     )
def Start_Button():
    #Cette fonction est destinée au bouton 'Start'
    Generateur()

       
def Exit_Button():
    #Cette fonction est destinée au bouton 'Exit'
    root.destroy()

def Save_Button():
    #Cette fonction est destinée au bouton 'Save'
    fic = open("save_liste.txt", "wb") 
    pc.dump(grille, fic)
    fic.close()
    

def Load_Button():
    #Cette fonction est destinée au bouton 'Load'
    global grille
    
    matrice2 = []
    fic = open("save_liste.txt", "rb")
    b = pc.load(fic)
    fic.close()
    for line in b:
        matrice2.append(line)
    
    grille = matrice2

    Actualisation_Inter()

# Fonctions associées aux déplacements

def Left_button():
    global grille
    grille = Empiler_Gauche(grille)
    grille = Combiner_Gauche(grille)
    grille = Empiler_Gauche(grille)
    grille = Generateur_Tuile(grille)
    Actualisation_Inter()
    game_Over()


def Right_button():
    global grille
    grille = Empiler_Droite(grille)
    grille = Combiner_Droite(grille)
    grille = Empiler_Droite(grille)
    grille = Generateur_Tuile(grille)
    Actualisation_Inter()
    game_Over()


def Up_button():
    global grille
    grille = Empiler_Haut(grille)
    grille = Combiner_Haut(grille)
    grille = Empiler_Haut(grille)
    grille = Generateur_Tuile(grille)
    Actualisation_Inter()
    game_Over()


def Down_button():
    global grille
    grille = Empiler_Bas(grille)
    grille = Combiner_Bas(grille)
    grille = Empiler_Bas(grille)
    grille = Generateur_Tuile(grille)
    Actualisation_Inter()
    game_Over()

## Fonctions associées aux tests au cours du jeu :

def Mouv_Hozizontale():
    """Regarde si on peut toujours se déplacer de manière horizontale"""
    for i in range (4):
        for j in range (1,3):
            if grille[i][j] == grille[i][j+1] or grille[i][j] == grille[i][j-1]:
                return True
    return False

def Mouv_Verticale():
    """Regarde si on peut toujours se déplacer de manière verticale"""
    for i in range (1,3):
        for j in range (4):
            if grille[i][j] == grille[i+1][j] or grille[i][j] == grille[i-1][j]:
                return True
    return False

def Vide_Mat():
    """Regarde s'il y a encore des espaces vides'"""
    for i in range(4):
        if 0 in grille[i]:
            return True
    return False

def game_Over():
    global score
    if any(2048 in row for row in grille):
        score = 1
        Affich_game_over()
    elif Vide_Mat()==False and Mouv_Hozizontale()==False and Mouv_Verticale()==False: 
        score = 0
        Affich_game_over()
    else:
        pass

def Affich_game_over(): #//créer un fond tout blanc pour afficher winner ou looser
    Interface()
    Actualisation_Inter()
    if score==1:
        game_over_frame = tk.Frame(background, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(game_over_frame,
                 text="Winner!",
                 bg="#ffcc00",
                 fg="#ffffff",
                 font=("Helvetica", 48, "bold")).pack()
    elif score==0:
        game_over_frame = tk.Frame(background, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(game_over_frame,
                 text="Loser!",
                 bg="#a39489",
                 fg="#ffffff",
                 font=("Helvetica", 48, "bold")).pack()
    else:
        pass

## Boutons :

Start = tk.Button(text="Start", 
                    height=1, width=4,
                    font=("Helvetica", "12","bold"),
                    command=Start_Button,bg="#fce130"
        
                  )
Start.grid(row=1, column=0)

Exit = tk.Button(text="Exit", 
                    height=1, width=4,
                    font=("Helvetica", "12","bold"),
                    command=Exit_Button,bg="#ff775c"
                  )
Exit.grid(row=1, column=1)


Save = tk.Button(text="Save", 
                    height=1, width=4,
                    font=("Helvetica", "12","bold"),command=Save_Button,bg="#f5b682"
                    
                  )
Save.grid(row=3, column=0)

Load = tk.Button(text="Load", 
                    height=1, width=4,
                    font=("Helvetica", "12","bold"),command=Load_Button,bg='#f5b682'

                  )
Load.grid(row=3, column=1)


    # Boutons déplacement  
    
Up = tk.Button(text="Up", 
                    height=1, width=4,
                    font=("Helvetica", "12","bold"),command=Up_button
                    
                  )
Up.grid(row=2, column=15)

Down = tk.Button(text="Down", 
                    height=1, width=4,
                    font=("Helvetica", "12","bold"),command=Down_button
                    
                  )
Down.grid(row=4, column=15)


Left = tk.Button(text="Left", 
                    height=1, width=4,
                    font=("Helvetica", "12","bold"),command=Left_button
                    
                  )
Left.grid(row=3, column=14)

Right = tk.Button(text="Right", 
                    height=1, width=4,
                    font=("Helvetica", "12","bold"),command=Right_button

                  )
Right.grid(row=3, column=16)


    # Background
        
background = tk.Frame(root, 
                bg="#a39489", 
                bd=3, width=570, 
                height=570
                ) 
                
background.grid(pady=20, columnspan=20,padx=20)

Interface()

root.mainloop()