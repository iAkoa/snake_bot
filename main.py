import pygame
import random
from display import afficher_serpent, afficher_nourriture, afficher_gameover
from constant import taille_cellule,largeur, hauteur, BLANC, NOIR, VERT, ROUGE
from nourriture import ft_nourriture
from bot import bot

# Initialisation de pygame
pygame.init()

# Création de la fenêtre du jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake")

# Horloge pour contrôler la vitesse du jeu
horloge = pygame.time.Clock()

# Fonction principale du jeu
def gameSnake():
	game_over = False
	# Position initiale du serpent
	serpent = [[largeur/2, hauteur/2]]
	# Direction initiale du serpent
	direction = 'droite'
	# Position initiale de la nourriture
	nourriture = ft_nourriture()
	# Boucle principale du jeu
	running = True
	while running:
		list_events = pygame.event.get()
		if len(list_events) > 0:
			event = list_events[0]
		# for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:  # Quitter le jeu en appuyant sur Échap
					running = False
				elif event.key == pygame.K_SPACE:
					game_over = False
					serpent = [[largeur/2, hauteur/2]]
					nourriture = ft_nourriture()
				elif event.key == pygame.K_UP and direction != 'bas':
					direction = 'haut'
				elif event.key == pygame.K_DOWN and direction != 'haut':
					direction = 'bas'
				elif event.key == pygame.K_LEFT and direction != 'droite':
					direction = 'gauche'
				elif event.key == pygame.K_RIGHT and direction != 'gauche':
					direction = 'droite'
		if not game_over:
			# Déplacement du serpent en fonction de sa direction
			direction = bot(direction, serpent, nourriture, 0)
			if direction == 'haut':
				serpent.insert(0, [serpent[0][0], serpent[0][1] - taille_cellule])
			elif direction == 'bas':
				serpent.insert(0, [serpent[0][0], serpent[0][1] + taille_cellule])
			elif direction == 'gauche':
				serpent.insert(0, [serpent[0][0] - taille_cellule, serpent[0][1]])
			elif direction == 'droite':
				serpent.insert(0, [serpent[0][0] + taille_cellule, serpent[0][1]])
			for tab in serpent[1:]:
				if serpent[0] == tab:
					game_over = True

			# Vérifier si le serpent a mangé la nourriture
			if serpent[0] == nourriture:
				# Générer une nouvelle position pour la nourriture
				nourriture = ft_nourriture()
				# Faire grandir le serpent en ajoutant une nouvelle cellule à la fin
			else:
				# Si le serpent n'a pas mangé la nourriture, supprimer la dernière cellule du serpent
				serpent.pop()
			# Effacement de l'écran
			fenetre.fill(NOIR)

			# Affichage du serpent et de la nourriture
			afficher_serpent(serpent)
			afficher_nourriture(nourriture)
		if len(serpent) > 0 and (serpent[0][0] < 0 or serpent[0][0] >= largeur or serpent[0][1] < 0 or serpent[0][1] >= hauteur):
			game_over = True
		if game_over:
			afficher_gameover()
		# Mise à jour de l'affichage
		pygame.display.flip()
		# Contrôle de la vitesse du jeu
		horloge.tick(20)
	pygame.quit()
# Lancement du jeu
gameSnake()

