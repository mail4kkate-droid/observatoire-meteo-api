
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


# Modèle ORM correspondant à la table "villes"
class Ville(Base):
    __tablename__ = "villes"

    # Identifiant unique de la ville
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Nom de la ville
    nom: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    # Coordonnées géographiques
    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    # Conserver le nom existant dans SQLite : "longuitude"
    longitude: Mapped[float] = mapped_column(
        "longuitude",
        Float,
        nullable=False
    )
