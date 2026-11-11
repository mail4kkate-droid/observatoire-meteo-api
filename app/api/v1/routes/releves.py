
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import releve_service
from app.api.v1.schemas.releve import (
    ReleveCreate,
    ReleveResponse
)


# Définir les routes des relevés météorologiques
router = APIRouter(
    prefix="/releves",
    tags=["Relevés météo"]
)


# GET : récupérer tous les relevés
@router.get("/", response_model=list[ReleveResponse])
def get_all(db: Session = Depends(get_db)):
    return releve_service.get_all(db)


# GET : récupérer les relevés d'une ville
@router.get(
    "/ville/{ville_id}",
    response_model=list[ReleveResponse]
)
def get_by_ville(
    ville_id: int,
    db: Session = Depends(get_db)
):
    return releve_service.get_by_ville(db, ville_id)


# GET : récupérer un relevé par son identifiant
@router.get("/{releve_id}", response_model=ReleveResponse)
def get_by_id(
    releve_id: int,
    db: Session = Depends(get_db)
):
    return releve_service.get_by_id(db, releve_id)


# POST : enregistrer un nouveau relevé
@router.post(
    "/",
    response_model=ReleveResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    data: ReleveCreate,
    db: Session = Depends(get_db)
):
    return releve_service.create(db, data)
