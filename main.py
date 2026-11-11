import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Créer notre application API
app = FastAPI(
    title="Observatoire Météo",
    description="API de consultation des relevés météo",
    version="1.0"
)


# Modèle Pydantic pour la réponse météo
class ReleveMeteo(BaseModel):
    ville: str
    temperature: float
    vitesse_vent: float
    date_heure: str


# Route d'accueil pour tester le serveur
@app.get("/")
def accueil():
    return {
        "message": "Bienvenue dans l'Observatoire Météo"
    }


# Chemin de la base de données
DB_PATH = Path(__file__).resolve().parent / "meteo.db"


# Route pour consulter la météo d'une ville
@app.get("/meteo/{ville}", response_model=ReleveMeteo)
def consulter_meteo(ville: str):

    # Ouvrir la base de données SQLite
    connexion = sqlite3.connect(DB_PATH)

    # Vérifier le chemin de la base de données
    print("Base utilisée :", DB_PATH)

    # Afficher les tables présentes dans la base
    curseur_test = connexion.cursor()
    curseur_test.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )
    print("Tables disponibles :", curseur_test.fetchall())

    try:
        curseur = connexion.cursor()

        # Rechercher le relevé le plus récent de la ville
        curseur.execute("""
            SELECT
                villes.nom,
                releves.temperature,
                releves.vitesse_vent,
                releves.date_heure
            FROM releves
            JOIN villes ON releves.ville_id = villes.id
            WHERE villes.nom = ? COLLATE NOCASE
            ORDER BY releves.date_heure DESC, releves.id DESC
            LIMIT 1
        """, (ville,))

        releve = curseur.fetchone()

    finally:
        # Toujours fermer la connexion
        connexion.close()

    # Retourner une erreur si aucun relevé n'existe
    if releve is None:
        raise HTTPException(
            status_code=404,
            detail="Aucun relevé trouvé pour cette ville"
        )

    # Construire la réponse JSON
    return ReleveMeteo(
        ville=releve[0],
        temperature=releve[1],
        vitesse_vent=releve[2],
        date_heure=releve[3]
    )
