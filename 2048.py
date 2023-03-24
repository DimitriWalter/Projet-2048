import tkinter as tk
import numpy as np
from random import randint

######################### Création de la grille #########################
'''
def new_grid() -> list:
    '''Crée une nouvelle grille vide'''
    return(np.zeros((4,4), dtype =  int))

def rdm_coord() -> tuple: 
    '''Choisis des coordonnées aléatoire'''
    x,y = randint(0,3), randint(0,3)
    return(x,y)

def rdm_block():
    '''Choisis un block aléatoire'''
    choix = [2,2,2,2,2,2,2,2,2,4] # 2 est 9 fois plus probable que 4
    return(choix[randint(0,1)])

def assign_block():
    '''Met le bloc choisis aléatoirement aux coordonnées aléatoire'''
    new_grid()[rdm_coord()] = rdm_block()

def print_grid():
    '''Affiche la grille dans la console'''
    return 
print(new_grid())

print(new_grid().shape)
'''

 # Interface graphique
    
racine = tk.Tk()
racine.title("2048")


    # Variables globales
        
cellules = []   # contient chaque détail de chaque tuile (couleur+nombre)
matrice = [] # contient les nombres présents sur la grille
end = None   # cette variable donnera si la partie est gagnée ou perdue,
              # 1 = gagné et 0 = perdu


# Fonctions premières  
       
def Creation_Interface():
    """Cette fonction va créer la plateforme de jeu"""
    global cellules
    for i in range (4):
        ligne = []
        for j in range (4):
            cellule_frame = tk.Frame(background, bg=c.COULEUR_CELLULE_VIDE, width=120, height=120)
            cellule_frame.grid(row=i, column=j, padx=5, pady=5)
            cellule_number = tk.Label(background, bg=c.COULEUR_CELLULE_VIDE)
            cellule_number.grid(row=i, column=j)
            cellule_data = {"frame": cellule_frame, "number": cellule_number}
            ligne.append(cellule_data)
        cellules.append(ligne)
    
    
def Actualisation_Interface():
    """Cette fonction va actualiser les couleurs/affichages dans le plateau"""
    global cellules
    for i in range (4):
        for j in range (4):
            valeur_cellule = matrice[i][j]
            if valeur_cellule == 0:
                cellules[i][j]["frame"].config(bg=c.COULEUR_CELLULE_VIDE)
                cellules[i][j]["number"].config(bg=c.COULEUR_CELLULE_VIDE, text="") 
            else:
                cellules[i][j]["frame"].config(bg=c.COULEURS_CELLULES[valeur_cellule])
                cellules[i][j]["number"].config(bg=c.COULEURS_CELLULES[valeur_cellule], 
                                             fg=c.NOMBRES_CELLULES[valeur_cellule],
                                             font=c.FONTS_CELLULES[valeur_cellule],
                                             text=str(valeur_cellule))
    

def Generateur_Tuile(mat):
    """ Cette fonction donne à matrice une tuile créée aléatoirement"""
    row = rd.randint(0,3)
    col = rd.randint(0,3)
    if Zero_In_Mat() == True:
        while mat[row][col]!=0:
            row = rd.randint(0,3)
            col = rd.randint(0,3)
        mat[row][col] = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    else:
        pass
    return mat


    # Empilation
def Empiler_Gauche(mat):
    """Place les tuiles vers la gauche"""
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
    """Place les tuiles vers la droite"""
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
    """Place les tuiles vers le haut"""
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
    """Place les tuiles vers le bas"""
    matrice2 = [[0]*4 for _ in range (4)]
    for j in range (4):
        pos = -1
        for i in range (1,5):
            if mat[-i][j] != 0:
                matrice2[pos][j] = mat[-i][j]
                pos-=1
    mat = matrice2
    return mat


racine.mainloop()

GRID_COULEUR = "#a39489" 
COULEUR_CELLULE_VIDE = "#c2b3a9" 
SCORE_LABEL_FONT = ("Verdana", 24)
SCORE_FONT =("Helvetica", 36, "bold")
GAME_OVER_FONT = ("Helvetica", 48, "bold")
GAME_OVER_FONT_COULEUR = "#ffffff" 
WINNER_BG = "#ffcc00" 
LOSER_BG = "#a39489" 


COULEURS_CELLULES = {
	2: "#fcefe6",
	4: "#f2e8cb",
	8: "#f5b682",
	16: "#f29446",
	32: "#ff775c",
	64: "#e64c2e",
	128: "#ede291",
	256: "#fce130",
	512: "#ffdb4a",
	1024: "#f0b922",
	2048: "#fad74d"
}

NOMBRES_CELLULES = {
	2: "#695c57",
	4: "#695c57",
	8: "#ffffff",
	16: "#ffffff",
	32: "#ffffff",
	64: "#ffffff",
	128: "#ffffff",
	256: "#ffffff",
	512: "#ffffff",
	1024: "#ffffff",
	2048: "#ffffff"
}

FONTS_CELLULES = {
	2: ("Helvetica", 55, "bold"),
	4: ("Helvetica", 55, "bold"),
	8: ("Helvetica", 55, "bold"),
	16: ("Helvetica", 50, "bold"),
	32: ("Helvetica", 50, "bold"),
	64: ("Helvetica", 50, "bold"),
	128: ("Helvetica", 45, "bold"),
	256: ("Helvetica", 45, "bold"),
	512: ("Helvetica", 45, "bold"),
	1024: ("Helvetica", 40, "bold"),
	2048: ("Helvetica", 40, "bold"),
}