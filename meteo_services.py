import requests
from pydantic import BaseModel, ValidationError


# Modèle des mesures météo actuelles
class CurrentWeatherModel(BaseModel):
    time: str
    temperature_2m: float
    wind_speed_10m: float


# Modèle de la réponse Open-Meteo
class WeatherResponseModel(BaseModel):
    latitude: float
    longitude: float
    current: CurrentWeatherModel


# Fonction pour récupérer et valider la météo
def obtenir_meteo(latitude: float, longitude: float):
    url = "https://api.open-meteo.com/v1/forecast"

    # Définir les paramètres de la requête
    parametres = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m"
    }

    try:
        # Envoyer la requête HTTP
        reponse = requests.get(
            url,
            params=parametres,
            timeout=10
        )

        # Vérifier le statut HTTP
        reponse.raise_for_status()

        # Convertir la réponse en dictionnaire
        donnees = reponse.json()

        # Valider les données avec Pydantic
        meteo = WeatherResponseModel.model_validate(donnees)

        # Retourner les données validées
        return meteo

    except requests.exceptions.RequestException as erreur:
        print("Erreur HTTP :", erreur)

    except ValidationError as erreur:
        print("Erreur de validation :", erreur)

    except ValueError as erreur:
        print("Erreur JSON :", erreur)

    # Retourner None en cas d'erreur
    return None


# Tester la fonction avec Saint-Quentin
resultat = obtenir_meteo(49.8489, 3.2876)

if resultat is not None:
    print("Température :", resultat.current.temperature_2m)
    print("Vent :", resultat.current.wind_speed_10m)