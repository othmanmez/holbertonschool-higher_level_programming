def replace_in_list(my_list, idx, element):
    # Vérifier si l'index est valide
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        # Remplacer l'élément à la position spécifiée
        my_list[idx] = element
        return my_list
