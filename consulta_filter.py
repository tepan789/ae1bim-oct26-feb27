"""Ejemplo de consulta con filter."""

from configuracion import FabricaSesion
from crear_base_entidades import Veterinario


sesion = FabricaSesion()

try:
    veterinarios = sesion.query(Veterinario).filter(Veterinario.apellidos == "Mendoza").all()

    print("VETERINARIOS CON APELLIDO MENDOZA")
    for veterinario in veterinarios:
        print(f"{veterinario.nombres} {veterinario.apellidos} - {veterinario.licencia_profesional}")
finally:
    sesion.close()
