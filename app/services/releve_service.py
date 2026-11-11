
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.releve import Releve
from app.repositories import releve_repository
from app.repositories import ville_repository
from app.api.v1.schemas.releve import ReleveCreate


# GET : récupérer tous les relevés météo
def get_all(db: Session):
    return releve_repository.get_all(db)


# GET : récupérer les relevés d'une ville
def get_by_ville(db: Session, ville_id: int):
    # Vérifier que la ville existe
    ville = ville_repository.get_by_id(db, ville_id)

    if ville is None:
        raise HTTPException(
            status_code=404,
            detail="Ville introuvable"
        )

    return releve_repository.get_by_ville(db, ville_id)


# GET : récupérer un relevé par son ID
def get_by_id(db: Session, releve_id: int):
    releve = releve_repository.get_by_id(db, releve_id)

    if releve is None:
        raise HTTPException(
            status_code=404,
            detail="Relevé introuvable"
        )

    return releve


# POST : enregistrer un nouveau relevé météo
def create(db: Session, data: ReleveCreate):
    # Vérifier que la ville existe avant l'enregistrement
    ville = ville_repository.get_by_id(db, data.ville_id)

    if ville is None:
        raise HTTPException(
            status_code=404,
            detail="Ville introuvable"
        )

    # Créer le relevé à partir des données validées
    releve = Releve(**data.model_dump())

    # Enregistrer le relevé dans SQLite
    return releve_repository.save(db, releve)
