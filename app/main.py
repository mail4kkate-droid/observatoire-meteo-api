
from fastapi import FastAPI

from app.api.v1.router import router


# Créer l'application FastAPI
app = FastAPI(
    title="L'Observatoire Météo",
    description="API de gestion des villes et des relevés météorologiques",
    version="1.0.0"
)


# Ajouter toutes les routes de l'API
app.include_router(router)


# Route d'accueil
@app.get("/", tags=["Accueil"])
def accueil():
    return {"message": "Bienvenue dans l'Observatoire Météo"}
