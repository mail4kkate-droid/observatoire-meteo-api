import requests

from pydantic import ValidationError

from pydantic import BaseModel


# Modèle pour les mesures météo actuelles
class CurrentWeatherModel(BaseModel):
    time: str
    temperature_2m: float
    wind_speed_10m: float


# Modèle pour la réponse de l'API
class WeatherResponseModel(BaseModel):
    latitude: float
    longitude: float
    current: CurrentWeatherModel


# Adresse de l'API météo
url = "https://api.open-meteo.com/v1/forecast"


# Paramètres pour Saint-Quentin
parametres = {
    "latitude": 49.8489,
    "longitude": 3.2876,
    "current": "temperature_2m,wind_speed_10m"
}


# Envoyer la requête GET
reponse = requests.get(
    url,
    params=parametres,
    timeout=10
)


# Vérifier le statut HTTP
reponse.raise_for_status()


# Convertir le JSON en dictionnaire Python
donnees = reponse.json()


# Afficher la réponse
print(donnees)


# Valider les données reçues avec Pydantic
meteo_validee = WeatherResponseModel.model_validate(donnees)


# Afficher les données validées
print("Température :", meteo_validee.current.temperature_2m)
print("Vent :", meteo_validee.current.wind_speed_10m)


# Créer une copie des données pour tester une erreur
donnees_invalides = donnees.copy()
# Modifier volontairement la température
donnees_invalides["current"] = donnees["current"].copy()
donnees_invalides["current"]["temperature_2m"] = "chaud"

try:
    # Valider les données incorrectes
    meteo_test = WeatherResponseModel.model_validate(
        donnees_invalides
    )

except ValidationError as erreur:
    # Afficher les erreurs de validation
    print("Erreur de validation :")
    print(erreur)