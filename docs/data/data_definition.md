# Definición de los datos

## Origen de los datos

- [ ] Los datos obtenidos para este proyecto corresponden a un conjunto de 500 imágenes de documentos de identidad. De estas, 250 imágenes representan documentos reales y las otras 250 son imágenes generadas artificialmente, donde se superponen datos falsos sobre documentos auténticos. Estos datos fueron recopilados de un servicio de almacenamiento en la nube llamado AWS.

## Especificación de los scripts para la carga de datos

- [ ] los datos se adquieren y preprocesan en el archivo exploaracion_generacion_data.ipynb

## Referencias a rutas o bases de datos origen y destino

- [ ] Para el desarrollo del proyecto, se cuenta con un conjunto de datos privado almacenado en Amazon S3 o Amazon Simple Storage Service. Este conjunto de datos consta de 250 documentos reales y 250 imágenes superpuestas, cada una de las cuales ha sido etiquetada y clasificada.

Debido a la sensibilidad de los datos y para garantizar la privacidad y confidencialidad, no se compartirá el conjunto de datos con terceros. El acceso y manejo de los datos se llevará a cabo siguiendo las políticas de seguridad y privacidad establecidas por la organización responsable del proyecto.

### Rutas de origen de datos

- [ ] Estos datos fueron recopilados de un servicio de almacenamiento en la nube llamado Amazon S3 hacia un entorno local.

### Base de datos de destino

- [ ] Una vez que los datos se descargaron al entorno local, se organizaron en una carpeta compartida en Google Drive para facilitar el acceso desde google colab. Esto se hizo para acceder fácilmente a los datos en el desarrollo del proyecto.

### Descripcion preprocesamiento 
- [ ] Se implementa una funcion en el archivo exploaracion_generacion_data.ipynb, despues de procesar las imegenes y cortas rolo los rotros se toma las imágenes de las carpetas "TRUE" y "FALSE", las escalará a un tamaño de 250x250 píxeles, las normalizará y realizará aumentación de datos. Luego, generará conjuntos de entrenamiento, prueba y validación con las proporciones mencionadas, mezclando la información de las dos carpetas.