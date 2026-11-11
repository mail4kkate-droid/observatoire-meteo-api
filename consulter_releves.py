
import sqlite3

# Se connecter à la base de données
connexion = sqlite3.connect("meteo.db")
curseur = connexion.cursor()

# Récupérer les relevés avec le nom de la ville
curseur.execute("""
    SELECT
        villes.nom,
        releves.temperature,
        releves.vitesse_vent,
        releves.date_heure
    FROM releves
    JOIN villes ON releves.ville_id = villes.id
    ORDER BY releves.date_heure DESC
""")

# Afficher les relevés enregistrés
for releve in curseur.fetchall():
    print(releve)

# Fermer la connexion
connexion.close()
