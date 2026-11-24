"""Ingreso de datos de ejemplo para la base de clinicas veterinarias."""

from datetime import date

from configuracion import FabricaSesion, motor
from crear_base_entidades import Base, Clinica, Consultorio, HistoriaClinica, Veterinario


def poblar_base_datos():
    """Guarda clinicas, consultorios, veterinarios e historias clinicas."""
    Base.metadata.create_all(motor)
    sesion = FabricaSesion()

    try:
        # Permite ejecutar el archivo varias veces sin duplicar los datos.
        if sesion.query(Clinica).count() > 0:
            print("La base de datos ya contiene informacion.")
            return

        clinica_quito = Clinica(
            nombre_comercial="Huellas Quito",
            direccion="Av. Naciones Unidas y Japon, Quito",
            veterinario_responsable="Dra. Ana Mendoza",
        )
        clinica_loja = Clinica(
            nombre_comercial="Patitas Loja",
            direccion="Calle Sucre 245, Loja",
            veterinario_responsable="Dr. Carlos Vega",
        )
        clinica_cuenca = Clinica(
            nombre_comercial="Amigos Peludos Cuenca",
            direccion="Av. Solano 610, Cuenca",
            veterinario_responsable="Dra. Sofia Torres",
        )

        consultorio_general = Consultorio(
            nombre_numero="Consultorio 1", especialidad_principal="Medicina general", clinica=clinica_quito
        )
        consultorio_cirugia = Consultorio(
            nombre_numero="Consultorio 2", especialidad_principal="Cirugia", clinica=clinica_quito
        )
        consultorio_dermatologia = Consultorio(
            nombre_numero="Consultorio A", especialidad_principal="Dermatologia", clinica=clinica_loja
        )
        consultorio_odontologia = Consultorio(
            nombre_numero="Consultorio B", especialidad_principal="Odontologia", clinica=clinica_loja
        )
        consultorio_exoticos = Consultorio(
            nombre_numero="Consultorio 3", especialidad_principal="Animales exoticos", clinica=clinica_cuenca
        )

        ana = Veterinario(
            nombres="Ana", apellidos="Mendoza", correo_electronico="ana.mendoza@huellas.ec",
            licencia_profesional="VET-001", consultorio=consultorio_general
        )
        luis = Veterinario(
            nombres="Luis", apellidos="Paredes", correo_electronico="luis.paredes@huellas.ec",
            licencia_profesional="VET-002", consultorio=consultorio_general
        )
        carlos = Veterinario(
            nombres="Carlos", apellidos="Vega", correo_electronico="carlos.vega@huellas.ec",
            licencia_profesional="VET-003", consultorio=consultorio_cirugia
        )
        sofia = Veterinario(
            nombres="Sofia", apellidos="Torres", correo_electronico="sofia.torres@patitas.ec",
            licencia_profesional="VET-004", consultorio=consultorio_dermatologia
        )
        diego = Veterinario(
            nombres="Diego", apellidos="Mora", correo_electronico="diego.mora@patitas.ec",
            licencia_profesional="VET-005", consultorio=consultorio_odontologia
        )
        elena = Veterinario(
            nombres="Elena", apellidos="Rios", correo_electronico="elena.rios@peludos.ec",
            licencia_profesional="VET-006", consultorio=consultorio_exoticos
        )

        historias = [
            HistoriaClinica(fecha_atencion=date(2026, 10, 2), diagnostico_principal="Gastritis leve", tratamiento_prescrito="Dieta blanda durante cinco dias", nombre_mascota="Milo", veterinario=ana),
            HistoriaClinica(fecha_atencion=date(2026, 10, 8), diagnostico_principal="Vacunacion preventiva", tratamiento_prescrito="Aplicar refuerzo anual", nombre_mascota="Luna", veterinario=ana),
            HistoriaClinica(fecha_atencion=date(2026, 10, 15), diagnostico_principal="Otitis", tratamiento_prescrito="Gotas oticas por siete dias", nombre_mascota="Rocky", veterinario=luis),
            HistoriaClinica(fecha_atencion=date(2026, 10, 20), diagnostico_principal="Fractura en pata", tratamiento_prescrito="Cirugia y reposo", nombre_mascota="Max", veterinario=carlos),
            HistoriaClinica(fecha_atencion=date(2026, 10, 25), diagnostico_principal="Control postoperatorio", tratamiento_prescrito="Continuar analgesico", nombre_mascota="Max", veterinario=carlos),
            HistoriaClinica(fecha_atencion=date(2026, 11, 1), diagnostico_principal="Dermatitis alergica", tratamiento_prescrito="Shampoo medicado", nombre_mascota="Nala", veterinario=sofia),
            HistoriaClinica(fecha_atencion=date(2026, 11, 5), diagnostico_principal="Dermatitis alergica", tratamiento_prescrito="Evitar alimento desencadenante", nombre_mascota="Milo", veterinario=sofia),
            HistoriaClinica(fecha_atencion=date(2026, 11, 10), diagnostico_principal="Sarro dental", tratamiento_prescrito="Limpieza dental programada", nombre_mascota="Toby", veterinario=diego),
            HistoriaClinica(fecha_atencion=date(2026, 11, 14), diagnostico_principal="Crecimiento excesivo de pico", tratamiento_prescrito="Recorte de pico y vitaminas", nombre_mascota="Kiwi", veterinario=elena),
        ]

        sesion.add_all([
            clinica_quito, clinica_loja, clinica_cuenca,
            consultorio_general, consultorio_cirugia, consultorio_dermatologia,
            consultorio_odontologia, consultorio_exoticos,
            ana, luis, carlos, sofia, diego, elena,
            *historias,
        ])
        sesion.commit()
        print("Datos ingresados correctamente.")
    except Exception:
        sesion.rollback()
        raise
    finally:
        sesion.close()


if __name__ == "__main__":
    poblar_base_datos()
