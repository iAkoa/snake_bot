directions = ['haut', 'bas', 'gauche', 'droite']
current_element = 'droite'  # L'élément actuel

current_index = directions.index(current_element)  # Trouver l'indice de l'élément actuel

next_index = (current_index + 1) % len(directions)  # Calculer l'indice de l'élément suivant

next_element = directions[next_index]  # Accéder à l'élément suivant
print(current_index + 1)
print(len(directions))
print(next_element)