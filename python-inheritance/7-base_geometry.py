#!/usr/bin/python3
"""Spécifie l'interpréteur à utiliser pour exécuter ce script."""


class BaseGeometry:
    """Classe de base pour les géométries."""

    def area(self):
        """Lève une exception indiquant que l'aire n'est pas implémentée."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide la valeur en vérifiant qu'elle est un entier et > 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        """Si la valeur est <= 0"""
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
