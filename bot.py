from constant import taille_cellule, droite, gauche, haut, bas
import copy
import random
from itertools import cycle


# def protect_snake(direction, serpent, nourriture, x, y):
# 	tmp = copy.deepcopy(serpent)


# 	# print('avant tmp[0][0] = ',tmp[0][0])
# 	# print('avant tmp[0][1] = ',tmp[0][1])
# 	if direction == 'haut' and serpent[0][0] - taille_cellule != 0:
# 		tmp.insert(0, [tmp[0][0], tmp[0][1] - taille_cellule])
# 	elif direction == 'bas' and tmp[0][0] + taille_cellule != 460:
# 		tmp.insert(0, [tmp[0][0], tmp[0][1] + taille_cellule])
# 	elif direction == 'gauche' and tmp[0][1] - taille_cellule != 0:
# 		tmp.insert(0, [tmp[0][0] - taille_cellule, tmp[0][1]])
# 	elif direction == 'droite' and tmp[0][1] + taille_cellule != 620:
# 		tmp.insert(0, [tmp[0][0] + taille_cellule, tmp[0][1]])
# 	# print('apres tmp[0][0] = ',tmp[0][0])
# 	# print('apres tmp[0][1] = ',tmp[0][1])
# 	for i in tmp[1:]:
# 		if tmp[0] == i:
# 			if direction == 'droite':
# 				if y > 0:
# 					direction = 'haut'
# 				else:
# 					direction = 'bas'
# 			elif direction == 'gauche':
# 				if y > 0:
# 					direction = 'haut'
# 				else:
# 					direction = 'bas'
# 			elif direction == 'haut':
# 				if x > 0:
# 					direction = 'gauche'
# 				else:
# 					direction = 'droite'
# 			elif direction == 'bas':
# 				if x > 0:
# 					direction = 'gauche'
# 				else:
# 					direction = 'droite'
# 	return direction

def protect_coast(direction, serpent, nourriture, x, y):
	if serpent[0][0] == gauche and serpent[0][1] != haut and serpent[0][1] != bas:
		if direction != 'bas':
			direction = 'haut'
		elif direction != 'haut':
			direction = 'bas'
	elif serpent[0][0] == droite and serpent[0][1] != haut and serpent[0][1] != bas:
		if direction != 'bas':
			direction = 'haut'
		elif direction != 'haut':
			direction = 'bas'
	elif serpent[0][1] == haut and serpent[0][0] != gauche and serpent[0][0] != droite:
		if direction != 'droite':
			direction = 'gauche'
		elif direction != 'gauche':
			direction = 'droite'
	elif serpent[0][1] == bas and serpent[0][0] != gauche and serpent[0][0] != droite:
		if direction != 'droite':
			direction = 'gauche'
		elif direction != 'gauche':
			direction = 'droite'
	elif serpent[0][0] == gauche and serpent[0][1] == haut:
		if direction == 'gauche':
			direction = 'bas'
		else:
			direction = 'droite'
	elif serpent[0][0] == droite and serpent[0][1] == bas:
		if direction == 'droite':
			direction = 'haut'
		else:
			direction == 'gauche'
	elif serpent[0][0] == droite and serpent[0][1] == haut:
		if direction == 'haut':
			direction = 'gauche'
		else:
			direction = 'bas'
	elif serpent[0][0] == gauche and serpent[0][1] == bas:
		if direction == 'bas':
			direction = 'droite'
		else:
			direction = 'haut'
	# print('direction dans coast = ', direction)
	return direction

def food_direction(direction, serpent, nourriture, x, y, directions):

	if abs(x) > abs(y):
		if x > 0:
			if direction != 'droite' and direction in directions:
				direction = 'gauche'
			elif y > 0 and direction != 'bas' and direction in directions:
				direction = 'haut'
			elif direction != 'gauche' and direction in directions:
				direction = 'droite'
			elif direction != 'haut' and direction in directions:
				direction = 'bas'
		else:
			if direction != 'gauche' and direction in directions:
				direction = 'droite'
			elif y > 0 and direction != 'bas' and direction in directions:
				direction = 'haut'
			elif direction != 'droite' and direction in directions:
				direction = 'gauche'
			elif direction != 'haut' and direction in directions:
				direction = 'bas'
	else:
		if y > 0:
			if direction != 'bas' and direction in directions:
				direction = 'haut'
			elif x > 0 and direction != 'droite' and direction in directions:
				direction = 'gauche'
			elif direction != 'haut' and direction in directions:
				direction = 'bas'
			elif direction != 'gauche' and direction in directions:
				direction = 'droite'
		else:
			if direction != 'haut' and direction in directions:
				direction = 'bas'
			elif x > 0 and direction != 'droite' and direction in directions:
				direction = 'gauche'
			elif direction != 'bas' and direction in directions:
				direction = 'haut'
			elif direction != 'gauche' and direction in directions:
				direction = 'droite'
	# print(direction)
	return direction

def check_next_case_collision(direction, current_direction, serpent, nourritur, directions):
	directions_cycle = cycle(directions)
	collision = True
	stop = 0
	while collision == True and stop < 4:
		print('<<<<<<<<<<<<<<<<<<<<STOP>>>>>>>>>>>>>>>', stop)
		tmp = copy.deepcopy(serpent)
		collision = False
		print('direction current ==', current_direction)
		print('0 >>> direction = ', direction)
		print('collision avant ==== ', collision)
		print('lst_directions  ===== ', directions)
		if direction == 'haut':
			tmp.insert(0, [tmp[0][0], tmp[0][1] - taille_cellule])
		elif direction == 'bas':
			tmp.insert(0, [tmp[0][0], tmp[0][1] + taille_cellule])
		elif direction == 'gauche':
			tmp.insert(0, [tmp[0][0] - taille_cellule, tmp[0][1]])
		elif direction == 'droite':
			tmp.insert(0, [tmp[0][0] + taille_cellule, tmp[0][1]])
		print(tmp[0][0])
		print(tmp[0][1])
		for i in tmp[1:]:
			if tmp[0] == i:
				collision = True
				# print('collision avec lui meme !')
			elif direction == 'droite' and tmp[0][0] == 640:
				# print('1 >> collision a droite')
				collision = True
			elif direction == 'gauche' and tmp[0][0] == -20:
				# print('2 >> collision a gauche')
				collision = True
			elif direction == 'haut' and tmp[0][1] == -20:
				# print('3 >> collision en haut')
				collision = True
			elif direction == 'bas' and tmp[0][1] == 480:
				# print('4 >> collision en bas')
				collision = True
			elif direction == 'droite' and current_direction == 'gauche':
				# print('security droite gauche')
				collision = True
			elif direction == 'gauche' and current_direction == 'droite':
				# print('security gauche droite')
				collision = True
			elif direction == 'haut' and current_direction == 'bas':
				# print('security haut bas')
				collision = True
			elif direction == 'bas' and current_direction == 'haut':
				# print('security bas haut')
				collision = True
		if collision == True:
			if direction in directions:
				directions.remove(direction)
				print('suprimance de ma direction ======= ',directions)
			direction = next(directions_cycle)
			print('5 NEXT direction >>>>>>>', direction)
		else:
			print('6 direction finale ====== ', direction)
			return direction
		print('collision avant ==== ', collision)
		stop += 1
	direction = directions[0]
	directions.remove(directions[0])
	if len(directions) == 0 and collision == True:
		print('eoooooooooooooooooooooooooooooooo')
		return 'NULL'
	return direction

def bot(direction, serpent, nourriture, recursive):
	tmp = copy.deepcopy(serpent)
	directions = ['haut', 'bas', 'gauche', 'droite']
	x = tmp[0][0] - nourriture[0]
	y = tmp[0][1] - nourriture[1]
	current_direction = direction
	recursive = recursive + 1
	print('RECURSIVE =============> N', recursive)
	print(direction)
	direction_test = direction
	while len(directions) != 0:
		direction = food_direction(direction, tmp, nourriture, x, y, directions)
		# if direction == 'haut' and tmp[0][1] == haut:
		# 	direction = protect_coast(direction, tmp, nourriture, x, y)
		# if direction == 'bas' and tmp[0][1] == bas:
		# 	direction = protect_coast(direction, tmp, nourriture, x, y)
		# if direction == 'gauche' and tmp[0][0] == gauche:
		# 	direction = protect_coast(direction, tmp, nourriture, x, y)
		# if direction == 'droite' and tmp[0][0] == droite:
		# 	direction = protect_coast(direction, tmp, nourriture, x, y)
		print('avant snake protect ========>', direction)
		# direction = protect_snake(direction, serpent, nourriture, x, y)
		direction = check_next_case_collision(direction, current_direction, tmp, nourriture, directions)
		# if direction
		print('direcition en output de check ===== ', direction)
		print('direcitions ===== ', directions)
		if direction == 'haut':
			tmp.insert(0, [tmp[0][0], tmp[0][1] - taille_cellule])
		elif direction == 'bas':
			tmp.insert(0, [tmp[0][0], tmp[0][1] + taille_cellule])
		elif direction == 'gauche':
			tmp.insert(0, [tmp[0][0] - taille_cellule, tmp[0][1]])
		elif direction == 'droite':
			tmp.insert(0, [tmp[0][0] + taille_cellule, tmp[0][1]])
		if direction == 'NULL':
			tmp.pop()
		if recursive < 3 and direction != 'NULL':
			direction_test = bot(direction, tmp, nourriture, recursive)
		# print('dsfdf')
		print(direction)
		if direction_test == 'NULL':
			direction = 'gauche'
		return direction
	# if len(directions) != 0:
	# 	bot(direction, tmp, nourriture, recursive)
	# else:
	# 	tmp.pop()
	# 	return False
	# print(recursive)
	# print('apres snake protect ========>', direction)