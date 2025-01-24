#!/usr/bin/python3
"""
Module qui définit une fonction pour additionner deux entiers.
"""

def add_integer(a, b=98):
    """
    Fonction qui additionne deux entiers (ou flottants).
    
    Paramètres:
    - a: Le premier nombre (entier ou flottant).
    - b: Le second nombre (entier ou flottant, par défaut 98).
    
    Retourne:
    La somme de a et b en tant qu'entier.
    """
    # Vérifier que 'a' est un entier ou un flottant
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Vérifier que 'b' est un entier ou un flottant
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Retourner la somme de a et b après les avoir convertis en entiers
    return int(a) + int(b)
