import pygame
import random
# Dimensions de la fenêtre du jeu
largeur = 640
hauteur = 480
droite = 620
haut = 0
bas = 460
gauche = 0

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)

# Taille de chaque cellule du serpent
taille_cellule = 20

# Position initiale du serpent
serpent = [[largeur/2, hauteur/2]]

nourriture = [[0 , 0]]

# Direction initiale du serpent
direction = 'droite'

# Création de la fenêtre du jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake")