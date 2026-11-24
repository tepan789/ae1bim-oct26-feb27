"""Ejemplo de consulta con and_."""

from sqlalchemy import and_

from configuracion import FabricaSesion
from crear_base_entidades import Veterinario


sesion = FabricaSesion()

try:
    veterinarios = (
        sesion.query(Veterinario)
        .filter(and_(Veterinario.nombres == "Ana", Veterinario.apellidos == "Mendoza"))
        .all()
    )

    print("VETERINARIO CON NOMBRES ANA Y APELLIDOS MENDOZA")
    for veterinario in veterinarios:
        print(f"{veterinario.nombres} {veterinario.apellidos} - {veterinario.correo_electronico}")
finally:
    sesion.close()
