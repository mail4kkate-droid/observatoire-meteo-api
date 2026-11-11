
import sqlite3
from pathlib import Path
from meteo_services import obtenir_meteo


# Coordonnées de Saint-Quentin
latitude = 49.8489
longitude = 3.2876

# Récupérer les données météo validées
meteo = obtenir_meteo(latitude, longitude)

# Vérifier que les données ont été récupérées
if meteo is not None:

    # Ouvrir la connexion SQLite
    DB_PATH = Path(__file__).resolve().parent / "meteo.db"
    print("base de donnees utilisee:", DB_PATH)
    connexion = sqlite3.connect(DB_PATH)

    # Activer les clés étrangères
    connexion.execute("PRAGMA foreign_keys = ON")

    # Rechercher l'identifiant de Saint-Quentin
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id FROM villes WHERE nom = ?",
        ("Saint-Quentin",)
    )

    ville = curseur.fetchone()

    if ville is not None:

        # Récupérer l'identifiant de la ville
        ville_id = ville[0]

        # Enregistrer le relevé météo
        curseur.execute("""
            INSERT INTO releves (
                ville_id,
                temperature,
                vitesse_vent,
                date_heure
            )
            VALUES (?, ?, ?, ?)
        """, (
            ville_id,
            meteo.current.temperature_2m,
            meteo.current.wind_speed_10m,
            meteo.current.time
        ))

        # Valider l'enregistrement
        connexion.commit()

        print("Relevé météo enregistré avec succès !")

    else:
        print("Ville introuvable dans la base de données.")

    # Fermer la connexion
    connexion.close()

else:
    print("Impossible de récupérer les données météo.")
