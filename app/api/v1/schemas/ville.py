
from pydantic import BaseModel, Field, ConfigDict


# Données nécessaires pour créer une ville (POST)
class VilleCreate(BaseModel):
    nom: str = Field(min_length=1)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


# Données pour remplacer une ville (PUT)
class VilleUpdate(VilleCreate):
    pass


# Données pour modifier partiellement une ville (PATCH)
class VillePatch(BaseModel):
    nom: str | None = Field(default=None, min_length=1)
    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)


# Format des données retournées par l'API (GET)
class VilleResponse(VilleCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
