
from fastapi import APIRouter

from app.api.v1.routes import villes, releves


# Regrouper toutes les routes de la version 1
router = APIRouter(prefix="/api/v1")

# Ajouter les routes des villes
router.include_router(villes.router)

# Ajouter les routes des relevés météo
router.include_router(releves.router)
