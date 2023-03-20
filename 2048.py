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

print(new_grid())

print(new_grid().shape)

########################## Interface graphique ##########################
root = tk.Tk()
root.title("2048")

def UI_grid():
    SIZE = new_grid().shape[0] # Taille de la matrice
    SIDE = 500

    back = tk.Canvas(background = "grey", height = SIDE, width = SIDE)
    back.grid(row = 0, column = 0, rowspan = SIZE, columnspan = SIZE)
    for x in range(SIZE):
        for y in range(SIZE):
            box = tk.Frame(background="ivory", height = SIDE//4, width = SIDE//4)
            box.grid(row=y, column=x)



UI_grid()

root.mainloop()