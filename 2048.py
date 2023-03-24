import tkinter as tk
import numpy as np
from random import randint

######################### Création de la grille #########################

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

########################## Interface graphique ##########################
root = tk.Tk()
root.resizable(width=False, height=False)
root.title("2048")

def UI_grid():
    grid = new_grid()
    SIZE = new_grid().shape[0] # Taille de la matrice
    SIDE = 500

    back = tk.Canvas(background = "grey", height = SIDE, width = SIDE)
    back.grid(row = 0, column = 0, rowspan = SIZE, columnspan = SIZE)
    for x in range(SIZE):
        for y in range(SIZE):
            box = tk.Frame()
            box_text = tk.Label(box, text = grid[x][y], height=SIZE*2-1, width=SIZE*4)
            box.grid(row=y, column=x)
            box_text.pack()

def play():
    assign_block()

def leave():
    root.destroy()


UI_grid()
playButton = tk.Button(text = "Play", command=play)
playButton.grid(row=5,column=0)
leaveButton = tk.Button(text = "Leave", command=leave)
leaveButton.grid(row=5, column=1)
print()

root.mainloop()

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