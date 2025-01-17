#!/usr/bin/python3

import marshal

# Fonction pour extraire et afficher les noms depuis le fichier .pyc
def print_names_from_pyc(pyc_file_path):
    # Ouvrir le fichier .pyc
    with open(pyc_file_path, 'rb') as f:
        # Le fichier .pyc commence par un en-tête de 16 octets qu'on ignore
        f.read(16)
        # Lire le bytecode restant
        bytecode = f.read()

    # Charger le bytecode dans un objet code
    code_obj = marshal.loads(bytecode)

    # Extraire les noms définis dans le code
    names = code_obj.co_names

    # Filtrer les noms (exclure ceux qui commencent par '__') et les trier
    valid_names = sorted(name for name in names if not name.startswith('__'))

    # Afficher chaque nom valide sur une nouvelle ligne
    for name in valid_names:
        print(name)

# Si ce script est exécuté directement (et non importé), alors...
if __name__ == "__main__":
    # Définir le chemin du fichier .pyc téléchargé
    pyc_file_path = '/tmp/hidden_4.pyc'

    # Appeler la fonction pour afficher les noms
    print_names_from_pyc(pyc_file_path)
