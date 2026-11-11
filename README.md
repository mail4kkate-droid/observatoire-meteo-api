
# L'Observatoire Météo — API REST

## Présentation

Ce projet est une API REST développée avec Python et FastAPI.

Elle permet de gérer des villes et leurs relevés météorologiques.

## Technologies utilisées

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Swagger UI

## Fonctionnalités

- Consulter la liste des villes
- Ajouter une ville
- Modifier les informations d'une ville
- Supprimer une ville
- Consulter les relevés météorologiques
- Ajouter des relevés météorologiques

## Architecture

Le projet utilise une architecture organisée en plusieurs couches :

- Models : modèles de données
- Schemas : validation des données
- Repositories : accès à la base de données
- Services : logique métier
- Routes : endpoints de l'API

## Installation

Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

## Démarrage

Depuis le dossier meteo :

```bash
python -m uvicorn app.main:app --reload
```

## Documentation API

Ouvrir dans le navigateur :

http://127.0.0.1:8000/docs

## Tests manuels

Les endpoints ont été testés avec Swagger UI.

Résultats :
- GET : 200 OK
- POST : 201 Created
- PUT : 200 OK
- DELETE : 204 No Content
