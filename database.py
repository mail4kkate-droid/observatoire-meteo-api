import sqlite3
from pathlib import Path

# Créer la connexion à la base des données SQLite
DB_PATH = Path(__file__).resolve().parent / "meteo.db"
connexion = sqlite3.connect(DB_PATH)

# Activer la vérification des clés étrangères
connexion.execute("PRAGMA foreign_keys = ON")


# Créer la table des villes
connexion.execute("""
CREATE TABLE IF NOT EXISTS villes (
id INTEGER PRIMARY KEY AUToIncrement,
nom TEXT NOT NULL,
latitude REAL NOT NULL,
longuitude REAL NOT NULL
)
""")


# Créer la table des rélevés météo
connexion.execute("""
CREATE TABLE IF NOT EXISTS releves(
id INTEGER PRIMARY KEY AUTOINCREMENT,
ville_id INTEGER NOT NULL,
temperature REAL NOT NULL,
vitesse_vent REAL NOT NULL,
date_heure TEXT NOT NULL,
FOREIGN KEY (ville_id) REFERENCES villes(id)
)
""")

# Enregistrer les modifications
connexion.commit()

# Fermer la connexion
connexion.close()


print("Base de données est créée avec succès !")