
from sqlalchemy import Integer, Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


# Modèle ORM correspondant à la table "releves"
class Releve(Base):
    __tablename__ = "releves"

    # Identifiant unique du relevé
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Référence à la ville associée au relevé
    ville_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("villes.id"),
        nullable=False
    )

    # Température mesurée en degrés Celsius
    temperature: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    # Vitesse du vent
    vitesse_vent: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    # Date et heure du relevé
    date_heure: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
