"""Ejemplo de consulta con order_by."""

from configuracion import FabricaSesion
from crear_base_entidades import HistoriaClinica


sesion = FabricaSesion()

try:
    historias = sesion.query(HistoriaClinica).order_by(HistoriaClinica.fecha_atencion.desc()).all()

    print("HISTORIAS CLINICAS ORDENADAS POR FECHA DESCENDENTE")
    for historia in historias:
        print(f"{historia.fecha_atencion} - {historia.nombre_mascota}: {historia.diagnostico_principal}")
finally:
    sesion.close()
