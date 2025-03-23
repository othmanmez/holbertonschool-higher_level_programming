# Python Server-Side Rendering - Task 04

Ce projet implémente un système de gestion de produits avec support de plusieurs sources de données (JSON, CSV, et SQLite) dans une application Flask.

## Description

Le système permet de :
- Afficher des produits depuis différentes sources de données
- Filtrer les produits par ID
- Gérer les erreurs de manière élégante
- Fournir une interface utilisateur cohérente

## Structure du Projet

```
python-server_side_rendering/
├── README.md
├── init_db.py
├── task_04_db.py
├── products.json
├── products.csv
├── products.db
└── templates/
    ├── header.html
    ├── footer.html
    └── product_display.html
```

## Sources de Données

Le système supporte trois sources de données différentes :

1. **JSON** (`products.json`) :
   - Format JSON avec une liste de produits
   - Chaque produit contient : id, name, category, price

2. **CSV** (`products.csv`) :
   - Format CSV avec en-têtes
   - Colonnes : id, name, category, price

3. **SQLite** (`products.db`) :
   - Base de données SQLite
   - Table Products avec colonnes : id, name, category, price

## Installation et Configuration

1. Assurez-vous d'avoir Python 3.x installé
2. Installez les dépendances :
   ```bash
   pip install Flask
   ```

3. Initialisez la base de données SQLite :
   ```bash
   python init_db.py
   ```

## Utilisation

1. Lancez l'application :
   ```bash
   python task_04_db.py
   ```

2. Accédez à l'application dans votre navigateur :
   - Page d'accueil : `http://localhost:5000`
   - Liste des produits : `http://localhost:5000/products?source=json`
   - Produit spécifique : `http://localhost:5000/products?source=json&id=1`

## Paramètres de Requête

- `source` : Source de données ('json', 'csv', ou 'sql')
- `id` : ID du produit (optionnel)

## Exemples d'URLs

- Tous les produits JSON : `/products?source=json`
- Tous les produits CSV : `/products?source=csv`
- Tous les produits SQLite : `/products?source=sql`
- Produit JSON spécifique : `/products?source=json&id=1`
- Produit CSV spécifique : `/products?source=csv&id=2`
- Produit SQLite spécifique : `/products?source=sql&id=3`

## Gestion des Erreurs

Le système gère les cas d'erreur suivants :
- Source invalide : "Wrong source. Please use 'json', 'csv', or 'sql'."
- Produit non trouvé : "Product not found"
- Erreurs de base de données : "No products found"
- Fichiers manquants : "No products found"

## Fonctionnalités

- Support de plusieurs sources de données
- Interface utilisateur cohérente
- Gestion robuste des erreurs
- Code modulaire et réutilisable
- Filtrage des produits par ID
- Affichage formaté des prix

## Structure de la Base de Données

Table Products :
```sql
CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
```

## Données de Test

Les données de test sont identiques dans toutes les sources :
- Laptop (Electronics, $799.99)
- Coffee Mug (Home Goods, $15.99)
- Headphones (Electronics, $99.99)
- Desk Chair (Furniture, $199.99) 