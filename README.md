# API-AWS
# Ejecución de una API Django

Este repositorio contiene una API construida con Django, un marco de trabajo web de alto nivel en Python. Este README proporcionará los pasos necesarios para configurar y ejecutar la API en tu entorno local.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python (preferiblemente Python 3.x)
- pip (el administrador de paquetes de Python)
- virtualenv (opcional, pero recomendado para aislar las dependencias del proyecto)

## Configuración del Entorno Virtual (Opcional)

Puedes configurar un entorno virtual para este proyecto para aislar sus dependencias del sistema global. Si no deseas hacer esto, puedes omitir esta sección.

1. Abre una terminal y navega al directorio del proyecto.
2. Ejecuta el siguiente comando para crear un nuevo entorno virtual:
3. Activar el entorno virtual:



3. Activar el entorno virtual:

```bash
python3 -m venv venv
```

## Instalación de Dependencias

Una vez que hayas configurado tu entorno virtual (si es necesario), instala las dependencias del proyecto utilizando `pip`:
```bash
pip install -r requirements.txt
```

## Configuración de la Base de Datos

Este proyecto utiliza SQLite lOCALMENTE  como base de datos predeterminada para simplificar la configuración. PostgreSQL DESPLEGADO , puedes modificar la configuración en el archivo `settings.py`.

Por defecto, la configuración de la base de datos se encuentra en `project_name/settings.py`. Puedes ajustar la configuración de la base de datos según tus necesidades.

## Ejecución de las Migraciones

Antes de ejecutar la API, necesitamos aplicar las migraciones para crear las tablas en la base de datos:

´´´
python manage.py migrate

´´´

