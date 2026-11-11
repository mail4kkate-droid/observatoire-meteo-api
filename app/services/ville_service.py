
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.ville import Ville
from app.repositories import ville_repository
from app.api.v1.schemas.ville import (
    VilleCreate,
    VilleUpdate,
    VillePatch
)


# GET : récupérer toutes les villes
def get_all(db: Session):
    return ville_repository.get_all(db)


# GET : récupérer une ville par son ID
def get_by_id(db: Session, ville_id: int):
    ville = ville_repository.get_by_id(db, ville_id)

    if ville is None:
        raise HTTPException(
            status_code=404,
            detail="Ville introuvable"
        )

    return ville


# POST : créer une nouvelle ville
def create(db: Session, data: VilleCreate):
    ville = Ville(**data.model_dump())
    return ville_repository.save(db, ville)


# PUT : remplacer toutes les données d'une ville
def replace(db: Session, ville_id: int, data: VilleUpdate):
    ville = get_by_id(db, ville_id)

    # Remplacer tous les champs modifiables
    for champ, valeur in data.model_dump().items():
        setattr(ville, champ, valeur)

    return ville_repository.update(db, ville)


# PATCH : modifier uniquement les champs fournis
def patch(db: Session, ville_id: int, data: VillePatch):
    ville = get_by_id(db, ville_id)

    # Exclure les champs absents de la requête
    modifications = data.model_dump(exclude_unset=True)

    # Refuser les valeurs nulles pour les champs obligatoires
    if any(valeur is None for valeur in modifications.values()):
        raise HTTPException(
            status_code=422,
            detail="Les champs ne peuvent pas être null"
        )

    for champ, valeur in modifications.items():
        setattr(ville, champ, valeur)

    return ville_repository.update(db, ville)


# DELETE : supprimer une ville
def delete(db: Session, ville_id: int):
    ville = get_by_id(db, ville_id)

    try:
        ville_repository.delete(db, ville)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Impossible de supprimer une ville avec des relevés"
        )

    return None
