# Python - Everything is an Object

Ce projet explore les concepts fondamentaux des objets en Python et leur comportement en mémoire.

## Concepts Clés

### Identifiants d'Objets
- La fonction `id()` permet d'obtenir l'identifiant unique d'un objet (adresse mémoire dans CPython)
- Les petits entiers sont mis en cache par Python (interning)
- Les chaînes de caractères peuvent être partagées (string interning)

### Comparaison d'Objets
- `==` compare les valeurs des objets
- `is` compare les identifiants des objets (adresses mémoire)

### Types Mutable vs Immutable
- **Mutable**: listes, dictionnaires, ensembles
  - Peuvent être modifiés après création
  - Les modifications in-place conservent l'identifiant
  - Les opérations créant un nouvel objet changent l'identifiant

- **Immutable**: tuples, chaînes, entiers, flottants
  - Ne peuvent pas être modifiés après création
  - Les opérations créent toujours de nouveaux objets

### Comportement des Listes
- L'assignation directe (`=`) crée une référence au même objet
- La concaténation (`+`) crée un nouvel objet
- Les modifications in-place (`+=`, `append()`) modifient l'objet existant

### Tuples
- Les tuples vides `()` sont uniques en Python
- Un tuple à un élément nécessite une virgule: `(1,)`
- Sans virgule, `(1)` est un entier, pas un tuple

## Exemples Pratiques

1. **Entiers et Interning**
```python
a = 89
b = 89
print(a is b)  # True (petits entiers mis en cache)
```

2. **Listes et Références**
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # [1, 2, 3, 4] (même objet)
```

3. **Modification de Liste**
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]  # Nouvel objet
print(l2)  # [1, 2, 3] (objet original inchangé)
```

## Points Importants

1. Python utilise le passage par référence pour les objets
2. Les objets mutables peuvent être modifiés via leurs références
3. Les opérations in-place sur les listes modifient l'objet existant
4. Les tuples vides sont uniques en Python
5. La copie d'une liste crée un nouvel objet avec les mêmes éléments 