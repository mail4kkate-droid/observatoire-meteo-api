
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import ville_service
from app.api.v1.schemas.ville import (
    VilleCreate,
    VilleUpdate,
    VillePatch,
    VilleResponse
)


# Définir les routes de gestion des villes
router = APIRouter(
    prefix="/villes",
    tags=["Villes"]
)


# GET : récupérer toutes les villes
@router.get("/", response_model=list[VilleResponse])
def get_all(db: Session = Depends(get_db)):
    return ville_service.get_all(db)


# GET : récupérer une ville par son identifiant
@router.get("/{ville_id}", response_model=VilleResponse)
def get_by_id(
    ville_id: int,
    db: Session = Depends(get_db)
):
    return ville_service.get_by_id(db, ville_id)


# POST : créer une nouvelle ville
@router.post(
    "/",
    response_model=VilleResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    data: VilleCreate,
    db: Session = Depends(get_db)
):
    return ville_service.create(db, data)


# PUT : remplacer les données d'une ville
@router.put("/{ville_id}", response_model=VilleResponse)
def replace(
    ville_id: int,
    data: VilleUpdate,
    db: Session = Depends(get_db)
):
    return ville_service.replace(db, ville_id, data)


# PATCH : modifier partiellement une ville
@router.patch("/{ville_id}", response_model=VilleResponse)
def patch(
    ville_id: int,
    data: VillePatch,
    db: Session = Depends(get_db)
):
    return ville_service.patch(db, ville_id, data)


# DELETE : supprimer une ville
@router.delete(
    "/{ville_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    ville_id: int,
    db: Session = Depends(get_db)
):
    ville_service.delete(db, ville_id)
    return None
