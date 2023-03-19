import tkinter as tk
import numpy as np
from random import randint

######################### Création de la grille #########################

grid = np.zeros((4,4), dtype = np.uint)

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
    grid[rdm_coord()] = rdm_block()




########################## Interface graphique ##########################
root = tk.Tk()
root.title("2048")


print(grid)

root.mainloop()