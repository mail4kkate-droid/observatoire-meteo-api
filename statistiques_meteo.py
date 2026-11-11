
import sqlite3

# Connexion à la base de données
connexion = sqlite3.connect("meteo.db")
curseur = connexion.cursor()

# Calculer les statistiques pour Saint-Quentin
curseur.execute("""
    SELECT
        villes.nom,
        COUNT(releves.id),
        MIN(releves.temperature),
        MAX(releves.temperature),
        AVG(releves.temperature)
    FROM releves
    JOIN villes ON releves.ville_id = villes.id
    WHERE villes.nom = ?
    GROUP BY villes.id, villes.nom
""", ("Saint-Quentin",))

# Récupérer le résultat
statistiques = curseur.fetchone()

# Afficher les statistiques
if statistiques is not None:
    print("Ville :", statistiques[0])
    print("Nombre de relevés :", statistiques[1])
    print("Température minimale :", statistiques[2])
    print("Température maximale :", statistiques[3])
    print("Température moyenne :", statistiques[4])
else:
    print("Aucun relevé trouvé.")

# Fermer la connexion
connexion.close()
