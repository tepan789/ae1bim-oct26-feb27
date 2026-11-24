"""Ejemplo de consulta con or_."""

from sqlalchemy import or_

from configuracion import FabricaSesion
from crear_base_entidades import HistoriaClinica


sesion = FabricaSesion()

try:
    historias = (
        sesion.query(HistoriaClinica)
        .filter(
            or_(
                HistoriaClinica.diagnostico_principal == "Dermatitis alergica",
                HistoriaClinica.nombre_mascota == "Milo",
            )
        )
        .all()
    )

    print("HISTORIAS CON DERMATITIS ALERGICA O MASCOTA MILO")
    for historia in historias:
        print(f"{historia.nombre_mascota}: {historia.diagnostico_principal}")
finally:
    sesion.close()
