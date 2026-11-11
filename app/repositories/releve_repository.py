
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.releve import Releve


# GET : récupérer tous les relevés météo
def get_all(db: Session) -> list[Releve]:
    return list(db.scalars(select(Releve)).all())


# GET : récupérer les relevés d'une ville
def get_by_ville(db: Session, ville_id: int) -> list[Releve]:
    requete = select(Releve).where(
        Releve.ville_id == ville_id
    )
    return list(db.scalars(requete).all())


# GET : rechercher un relevé par son identifiant
def get_by_id(db: Session, releve_id: int) -> Releve | None:
    return db.get(Releve, releve_id)


# POST : enregistrer un nouveau relevé météo
def save(db: Session, releve: Releve) -> Releve:
    db.add(releve)
    db.commit()
    db.refresh(releve)
    return releve
