import pygame
from constant import taille_cellule, VERT, fenetre, ROUGE, largeur, hauteur
from nourriture import ft_nourriture

# Fonction pour afficher le serpent
def afficher_serpent(serpent):
	for position in serpent:
		pygame.draw.rect(fenetre, VERT, (position[0], position[1], taille_cellule, taille_cellule))

# Fonction pour afficher la nourriture
def afficher_nourriture(nourriture):
	pygame.draw.rect(fenetre, ROUGE, (nourriture[0], nourriture[1], taille_cellule, taille_cellule))

def afficher_gameover():
	font_gameover = pygame.font.Font(None, 36)  # Définissez la police et la taille du texte
	text_gameover = font_gameover.render("Game Over", True, (255, 255, 255))  # Définissez le texte, la couleur (rouge ici)
	text_rect_gameover = text_gameover.get_rect(center=(largeur // 2, hauteur // 3))  # Positionnez le texte au milieu de l'écran
	fenetre.blit(text_gameover, text_rect_gameover)  # Affichez le texte sur la fenêtre

	font_pause = pygame.font.Font(None, 24)  # Définissez la police et la taille du texte
	text_pause = font_pause.render("SPACE & REPLAY", True, (255, 255, 255))  # Définissez le texte, la couleur (rouge ici)
	text_rect_pause = text_pause.get_rect(center=(largeur // 2, hauteur / 1.5))  # Positionnez le texte au milieu de l'écran
	fenetre.blit(text_pause, text_rect_pause)  # Affichez le texte sur la fenêtre
