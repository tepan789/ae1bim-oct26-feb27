"""Configuracion de la conexion a la base de datos SQLite."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# El archivo clinicas_veterinarias.db se creara en esta misma carpeta.
motor = create_engine("sqlite:///clinicas_veterinarias.db", echo=False)
FabricaSesion = sessionmaker(bind=motor)
