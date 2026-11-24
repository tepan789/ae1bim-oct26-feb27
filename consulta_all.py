"""Consulta all: clinicas y numero de historias clinicas asociadas."""

from sqlalchemy import func

from configuracion import FabricaSesion
from crear_base_entidades import Clinica, Consultorio, HistoriaClinica, Veterinario


sesion = FabricaSesion()

try:
    resultados = (
        sesion.query(Clinica, func.count(HistoriaClinica.id).label("total_historias"))
        .outerjoin(Clinica.consultorios)
        .outerjoin(Consultorio.veterinarios)
        .outerjoin(Veterinario.historias_clinicas)
        .group_by(Clinica.id)
        .order_by(Clinica.nombre_comercial)
        .all()
    )

    print("CLINICAS Y NUMERO DE HISTORIAS CLINICAS")
    for clinica, total_historias in resultados:
        print(f"{clinica.nombre_comercial}: {total_historias} historia(s) clinica(s)")
finally:
    sesion.close()
