# Red de clinicas veterinarias con SQLAlchemy

Proyecto desarrollado con Python, SQLite y el ORM SQLAlchemy.

Repositorio del trabajo: [tepan789/ae1bim-oct26-feb27](https://github.com/tepan789/ae1bim-oct26-feb27).

## Entidades

- Clinica: posee uno o varios consultorios.
- Consultorio: pertenece a una clinica y posee uno o varios veterinarios.
- Veterinario: pertenece a un consultorio y elabora historias clinicas.
- HistoriaClinica: pertenece a un veterinario.

## Ejecucion

Abra PowerShell en esta carpeta. Instale SQLAlchemy, cree las tablas y cargue
los datos de ejemplo; luego ejecute las consultas que desee:

```powershell
py -3 -m pip install SQLAlchemy
py -3 crear_base_entidades.py
py -3 poblar_base.py
py -3 consulta_all.py
py -3 consulta_filter.py
py -3 consulta_order_by.py
py -3 consulta_or.py
py -3 consulta_and.py
```

La consulta `consulta_all.py` presenta cada clinica junto con la cantidad de
historias clinicas atendidas por sus veterinarios.

Los datos quedan en `clinicas_veterinarias.db` dentro de la carpeta desde la
que se ejecutan los comandos. Si vuelve a ejecutar `crear_base_entidades.py`,
se recrean las tablas y se borran los datos anteriores.
