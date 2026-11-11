import sqlite3
from pathlib import Path

# Connexion à la base des données
DB_PATH = Path(__file__).resolve().parent / "meteo.db"
connexion = sqlite3.connect(DB_PATH)
curseur = connexion.cursor()


# Ajouter une ville dans la table des villes
curseur.execute("""
    INSERT INTO villes (nom, latitude, longuitude)
    VALUES(?, ?, ?)
""", ("Saint-Quentin", 49.8489, 3.2876))


# Enregistrer les modifications
connexion.commit()

# Lire les villes enregistrées
curseur.execute("SELECT * FROM villes")

# Afficher les résultats 
for ville in curseur.fetchall():
    print(ville)

# Fermer la connexion
connexion.close()
