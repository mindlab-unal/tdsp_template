# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** img_super
- **Plataforma de despliegue:** La infraestructura utilizada para el despliegue del modelo "img_super" se basa en contenedores Docker y se implementa mediante la plataforma Uvicorn y FastAPI.
- **Requisitos técnicos:**  Los archivos relevantes para la configuración de la infraestructura se encuentran en las siguientes rutas dentro del proyecto:

Dockerfile: El archivo Dockerfile se encuentra en la ruta \src\img_super\Dockerfile. Este archivo contiene las instrucciones necesarias para construir la imagen del contenedor. En este caso, se utiliza la imagen base de Python 3.11-slim y se instalan las dependencias necesarias, como FastAPI, TensorFlow y otras bibliotecas requeridas por el modelo.

requirements.txt: El archivo requirements.txt se encuentra en la ruta \src\img_super\requirements.txt. Este archivo enumera las dependencias y versiones específicas que deben instalarse en el entorno del contenedor. Al construir la imagen del contenedor, se utiliza este archivo para instalar las bibliotecas necesarias, como FastAPI, TensorFlow y otras dependencias.

- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)

![methods](images/svg.svg)
## Código de despliegue

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
