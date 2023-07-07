import random
from constant import largeur, hauteur, taille_cellule

# Position initiale de la nourriture
def ft_nourriture():
    nourriture = [random.randint(0, (largeur - taille_cellule) // taille_cellule) * taille_cellule,
                random.randint(0, (hauteur - taille_cellule) // taille_cellule) * taille_cellule]
    return nourriture