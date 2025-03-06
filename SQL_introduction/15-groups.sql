-- Compter le nombre d'enregistrements pour chaque score dans la table second_table
-- Afficher le score et le nombre d'enregistrements avec le label "number"
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

