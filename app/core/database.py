
from pathlib import Path
from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Chemin vers la base de données SQLite existante
DB_PATH = Path(__file__).resolve().parents[2] / "meteo.db"

# Créer le moteur de connexion à SQLite
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Activer la vérification des clés étrangères
@event.listens_for(engine, "connect")
def activer_cles_etrangeres(dbapi_connection, connection_record):
    curseur = dbapi_connection.cursor()
    curseur.execute("PRAGMA foreign_keys=ON")
    curseur.close()


# Configurer les sessions SQLAlchemy
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)


# Classe de base pour les modèles ORM
class Base(DeclarativeBase):
    pass


# Fournir une session à FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
