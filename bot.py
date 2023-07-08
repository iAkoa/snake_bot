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

def food_direction(serpent, nourriture, directions):
	x = serpent[0][0] - nourriture[0]
	y = serpent[0][1] - nourriture[1]
	# if direction in directions:
		# print('directions in food ?? ', directions)
		# print('direction in food ??', direction)
		# print('currrnt_direction in food ??', current_direction)
	if abs(x) > abs(y):
		if x > 0:
			print("1")
			if 'gauche' in directions:
				return 'gauche'
			elif y > 0 and 'haut' in directions:
				return 'haut'
			elif 'droite' in directions:
				return 'droite'
			elif 'bas' in directions:
				return 'bas'
			elif 'haut' in directions:
				return 'haut'
		else:
			print("2")
			if 'droite' in directions:
				return 'droite'
			elif y > 0 and 'haut' in directions:
				return 'haut'
			elif 'gauche' in directions:
				return 'gauche'
			elif 'bas' in directions:
				return 'bas'
			elif 'haut' in directions:
				return 'haut'
				
	else:
		if y > 0:
			print("3")
			if 'haut' in directions:
				return 'haut'
			elif x > 0 and 'gauche' in directions:
				return 'gauche'
			elif 'bas' in directions:
				return 'bas'
			elif 'droite' in directions:
				return 'droite'
			elif 'haut' in directions:
				return 'gauche'
		else:
			print("4")
			if 'bas' in directions:
				return 'bas'
			elif x > 0 and 'gauche' in directions:
				return 'gauche'
			elif 'haut' in directions:
				return 'haut'
			elif 'droite' in directions:
				return 'droite'
			elif 'gauche' in directions:
				return 'gauche'
	# print('direction fin de food = ', direction)
	return 'NULL'

def check_next_case_collision(new_direction, current_direction, serpent, nourritur, new_s):
	tmp = copy.deepcopy(serpent)
	# print('direction in next_collision === ', direction)
	# print(tmp)
	collision = False
	# print('serpent avant check == ', tmp[0][0])
	# print('serpent avant check == ', tmp[0][1])
	if new_direction == 'haut':
		tmp.insert(0, [tmp[0][0], tmp[0][1] - taille_cellule])
	elif new_direction == 'bas':
		tmp.insert(0, [tmp[0][0], tmp[0][1] + taille_cellule])
	elif new_direction == 'gauche':
		tmp.insert(0, [tmp[0][0] - taille_cellule, tmp[0][1]])
	elif new_direction == 'droite':
		tmp.insert(0, [tmp[0][0] + taille_cellule, tmp[0][1]])
	# print('serpent == ',serpent)
	# print(tmp[0][1])
	for i in tmp[1:]:
		if tmp[0] == i:
			collision = True
			# print('collision avec lui meme !')
		elif new_direction == 'droite' and tmp[0][0] == 640:
			# print('1 >> collision a droite')
			collision = True
		elif new_direction == 'gauche' and tmp[0][0] == -20:
			# print('2 >> collision a gauche')
			collision = True
		elif new_direction == 'haut' and tmp[0][1] == -20:
			# print('3 >> collision en haut')
			collision = True
		elif new_direction == 'bas' and tmp[0][1] == 480:
			# print('4 >> collision en bas')
			collision = True
		elif new_direction == 'droite' and current_direction == 'gauche':
			# print('security droite gauche')
			collision = True
		elif new_direction == 'gauche' and current_direction == 'droite':
			# print('security gauche droite')
			collision = True
		elif new_direction == 'haut' and current_direction == 'bas':
			# print('security haut bas')
			collision = True
		elif new_direction == 'bas' and current_direction == 'haut':
			# print('security bas haut')
			collision = True
		elif new_direction == 'NULL':
			collision = True
	return collision

def bot(direction, serpent, nourriture, recursive):
	lst_directions = ['haut', 'bas', 'gauche', 'droite']
	directions_cycle = cycle(lst_directions)
	new_direction = direction
	current_direction = direction
	recursive_direction = direction
	recursive_test = recursive
	recursive = recursive + 1
	print('RECURSIVE =============> N', recursive)
	print('DEBUT ==============================> ')
	i = 0
	while len(lst_directions) != 0 and i < 4:
		print('[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]')
		print('DIRECTIONS ===== ', lst_directions)
		print('i =========', i)
		# recursive = recursive_test
		# if direction == 'haut' and tmp[0][1] == haut:
		# 	direction = protect_coast(direction, tmp, nourriture, x, y)
		# if direction == 'bas' and tmp[0][1] == bas:
		# 	direction = protect_coast(direction, tmp, nourriture, x, y)
		# if direction == 'gauche' and tmp[0][0] == gauche:
		# 	direction = protect_coast(direction, tmp, nourriture, x, y)
		# if direction == 'droite' and tmp[0][0] == droite:
		# 	direction = protect_coast(direction, tmp, nourriture, x, y)
		new_direction = food_direction(serpent, nourriture, lst_directions)
		print('current_direction apres food_direction = ',current_direction)
		print('new_direction apres food_direction = ',new_direction)
		collision = check_next_case_collision(new_direction, current_direction, serpent, nourriture, lst_directions)
		print('collision = ', collision)
		if collision == False:
			if recursive < 30:
				recursive_direction = bot(direction, serpent, nourriture, recursive)
				if recursive_direction != 'NULL':
					return new_direction
		elif collision == True:
			# print('direction avant remove = ',direction)
			print(lst_directions)
			if new_direction in lst_directions:
				lst_directions.remove(new_direction)
		i = i + 1
	return new_direction