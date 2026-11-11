
from pydantic import BaseModel, Field, ConfigDict


# Données nécessaires pour enregistrer un relevé météo
class ReleveCreate(BaseModel):
    ville_id: int = Field(gt=0)
    temperature: float
    vitesse_vent: float = Field(ge=0)
    date_heure: str = Field(min_length=1)


# Format des données retournées par l'API
class ReleveResponse(ReleveCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
