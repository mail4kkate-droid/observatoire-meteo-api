
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.ville import Ville


# GET : récupérer toutes les villes
def get_all(db: Session) -> list[Ville]:
    return list(db.scalars(select(Ville)).all())


# GET : rechercher une ville par son identifiant
def get_by_id(db: Session, ville_id: int) -> Ville | None:
    return db.get(Ville, ville_id)


# POST : enregistrer une nouvelle ville
def save(db: Session, ville: Ville) -> Ville:
    db.add(ville)
    db.commit()
    db.refresh(ville)
    return ville


# PUT / PATCH : enregistrer les modifications d'une ville
def update(db: Session, ville: Ville) -> Ville:
    db.commit()
    db.refresh(ville)
    return ville


# DELETE : supprimer une ville
def delete(db: Session, ville: Ville) -> None:
    db.delete(ville)
    db.commit()
