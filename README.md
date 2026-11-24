# Red de clinicas veterinarias con SQLAlchemy

Proyecto desarrollado con Python, SQLite y el ORM SQLAlchemy.

Fork: https://github.com/tepan789/ae1bim-oct26-feb27

## Entidades

- Clinica: posee uno o varios consultorios.
- Consultorio: pertenece a una clinica y posee uno o varios veterinarios.
- Veterinario: pertenece a un consultorio y elabora historias clinicas.
- HistoriaClinica: pertenece a un veterinario.

## Ejecucion

Instale la dependencia y, desde esta carpeta, ejecute los archivos en este orden:

```powershell
py -3 -m pip install -r requirements.txt
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

El archivo `clinicas_veterinarias.db` se crea en la carpeta desde la que se
ejecutan los comandos. Al ejecutar nuevamente `crear_base_entidades.py`, las
tablas se recrean y se pierden los datos anteriores.
