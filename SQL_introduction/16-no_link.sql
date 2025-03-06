-- Sélectionner les enregistrements de la table second_table où la colonne name n'est pas vide
-- Afficher le score et le nom (dans cet ordre)
-- Les résultats sont triés par score de manière décroissante
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

