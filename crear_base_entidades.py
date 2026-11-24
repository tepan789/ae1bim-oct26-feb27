"""Entidades de la red de clinicas veterinarias y creacion de la base."""

from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from configuracion import motor


class Base(DeclarativeBase):
    pass


class Clinica(Base):
    __tablename__ = "clinicas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre_comercial: Mapped[str] = mapped_column(String(100), nullable=False)
    direccion: Mapped[str] = mapped_column(String(150), nullable=False)
    veterinario_responsable: Mapped[str] = mapped_column(String(100), nullable=False)

    consultorios: Mapped[list["Consultorio"]] = relationship(
        back_populates="clinica", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Clinica(nombre_comercial='{self.nombre_comercial}')"


class Consultorio(Base):
    __tablename__ = "consultorios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre_numero: Mapped[str] = mapped_column(String(50), nullable=False)
    especialidad_principal: Mapped[str] = mapped_column(String(80), nullable=False)
    clinica_id: Mapped[int] = mapped_column(ForeignKey("clinicas.id"), nullable=False)

    clinica: Mapped["Clinica"] = relationship(back_populates="consultorios")
    veterinarios: Mapped[list["Veterinario"]] = relationship(
        back_populates="consultorio", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Consultorio(nombre_numero='{self.nombre_numero}')"


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombres: Mapped[str] = mapped_column(String(60), nullable=False)
    apellidos: Mapped[str] = mapped_column(String(60), nullable=False)
    correo_electronico: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    licencia_profesional: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    consultorio_id: Mapped[int] = mapped_column(ForeignKey("consultorios.id"), nullable=False)

    consultorio: Mapped["Consultorio"] = relationship(back_populates="veterinarios")
    historias_clinicas: Mapped[list["HistoriaClinica"]] = relationship(
        back_populates="veterinario", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Veterinario(nombres='{self.nombres}', apellidos='{self.apellidos}')"


class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fecha_atencion: Mapped[date] = mapped_column(Date, nullable=False)
    diagnostico_principal: Mapped[str] = mapped_column(String(180), nullable=False)
    tratamiento_prescrito: Mapped[str] = mapped_column(String(220), nullable=False)
    nombre_mascota: Mapped[str] = mapped_column(String(80), nullable=False)
    veterinario_id: Mapped[int] = mapped_column(ForeignKey("veterinarios.id"), nullable=False)

    veterinario: Mapped["Veterinario"] = relationship(back_populates="historias_clinicas")

    def __repr__(self):
        return f"HistoriaClinica(mascota='{self.nombre_mascota}', fecha='{self.fecha_atencion}')"


if __name__ == "__main__":
    # Se eliminan solo las tablas de esta base para generar una practica limpia.
    Base.metadata.drop_all(motor)
    Base.metadata.create_all(motor)
    print("Base de datos creada correctamente.")
