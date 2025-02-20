Serveur HTTP Simple avec Python
Ce projet met en place un serveur HTTP simple en utilisant le module http.server de Python. Il permet de répondre à différentes requêtes HTTP, d'envoyer des données JSON et de gérer des points de terminaison spécifiques.

Objectifs
Créer un serveur HTTP basique avec Python.
Servir des réponses en texte et en JSON.
Gérer des points de terminaison comme /status et /data.
Fournir une gestion des erreurs avec des réponses HTTP appropriées (ex. 404 pour les points de terminaison inconnus).
Fonctionnalités
Serveur HTTP : Utilisation de http.server pour gérer les requêtes.
Réponse textuelle : Le serveur répond avec un message simple à l'URL racine (/).
Serveur JSON : Le serveur répond avec des données JSON à l'endpoint /data.
État de l'API : Le serveur répond avec un message "OK" à l'endpoint /status.
Gestion des erreurs : Si un utilisateur tente d'accéder à un point de terminaison inconnu, une erreur 404 avec le message "Endpoint not found" est renvoyée.

