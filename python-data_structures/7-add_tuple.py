#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Gestion du tuple a
    if len(tuple_a) == 0:
        
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:

        tuple_a = (tuple_a[0], 0)

    # Gestion du tuple b

    if len(tuple_b) == 0:

        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)

    # Addition des éléments des tuples
    final_tuple = (int(tuple_a[0]) + int(tuple_b[0]),
                   int(tuple_a[1]) + int(tuple_b[1]))

    return final_tuple
