# Python - Variable Annotations

Ce projet explore l'utilisation des annotations de type en Python 3, qui permettent de spécifier les types des variables, des paramètres de fonction et des valeurs de retour.

## Concepts Clés

### Annotations de Type
- Les annotations de type permettent de documenter le code et d'améliorer sa lisibilité
- Elles aident les outils d'analyse statique comme mypy à détecter les erreurs potentielles
- Elles ne sont pas vérifiées à l'exécution par défaut (Python est toujours un langage à typage dynamique)

### Types de Base
- `int`: Entiers
- `float`: Nombres à virgule flottante
- `str`: Chaînes de caractères
- `bool`: Valeurs booléennes

### Types Complexes
- `List[T]`: Liste d'éléments de type T
- `Tuple[T1, T2, ...]`: Tuple avec des éléments de types spécifiques
- `Union[T1, T2, ...]`: Type qui peut être l'un des types spécifiés
- `Callable[[Arg1, Arg2, ...], ReturnType]`: Type de fonction

### Duck Typing
- Python utilise le "duck typing": si un objet se comporte comme un canard (a les méthodes attendues), il est traité comme un canard
- Les annotations de type peuvent spécifier des interfaces (comme `Iterable`, `Sequence`) plutôt que des types concrets

## Exemples

### Fonction Simple avec Annotations
```python
def add(a: float, b: float) -> float:
    return a + b
```

### Variables avec Annotations
```python
name: str = "John"
age: int = 30
height: float = 1.75
```

### Types Complexes
```python
from typing import List, Union, Tuple

# Liste de nombres (entiers ou flottants)
numbers: List[Union[int, float]] = [1, 2.5, 3, 4.7]

# Tuple avec une chaîne et un nombre
person: Tuple[str, int] = ("Alice", 25)
```

## Validation avec mypy

mypy est un vérificateur de type statique pour Python qui peut détecter les erreurs de type avant l'exécution du code.

Installation:
```bash
pip install mypy
```

Utilisation:
```bash
mypy mon_fichier.py
```

## Points Importants

1. Les annotations de type sont facultatives en Python
2. Elles n'affectent pas le comportement du code à l'exécution
3. Elles sont utiles pour la documentation et l'analyse statique
4. Python 3.5+ prend en charge nativement les annotations de type
5. Le module `typing` fournit des types génériques et des utilitaires pour les annotations 