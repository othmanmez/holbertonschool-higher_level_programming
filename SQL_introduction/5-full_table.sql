-- Afficher la structure de la table first_table en interrogeant la table information_schema
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH 
FROM information_schema.columns 
WHERE table_schema = '$1' AND table_name = 'first_table';

