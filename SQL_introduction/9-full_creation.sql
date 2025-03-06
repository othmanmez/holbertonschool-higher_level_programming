-- Créer la table second_table si elle n'existe pas
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

-- Ajouter les enregistrements dans la table second_table
INSERT INTO second_table (id, name, score) VALUES
  (1, 'John', 10),
 

