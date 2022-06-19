# Data Report

Este documento muestra los resultados del EDA.

## General summary of the data

Tenemos 115448 imagenes de las cuales, en el csv, hay 38496 con valores únicos, pues hay 3 filas por imagen. Cada fila es la mascara de cada uno de los 3 organos que se segmentan en cada imagen, y del total de datos, solo en 33913 se cuenta con la máscara de segmentación. Esto ocurre porque la mayoria de imagenes solo son negras, y no se observa nada en ellas para poder segmentar correctamente. 

De cada paciente se tienen mínimo 100 imágenes, y el promedio de imágenes por paciente es un poco mas de 400. Del día de tratamiento donde mas imágenes se tienen es el día 0 y el día 20, y la mayoria de pacientes tienen 144 imágenes por día. 
## Data quality summary
Las imágenes en su mayoria tienen un tamaño de 266px x 266px ó de 360px x 310px. Con respecto a las imágenes como tal, algunas muestran de manera muy clara todos los organos a segmentar, otras no muestran todos los organos, también pasa que el tamaño de los organos varía en cada imagen. Finalmente, hay que tener presente que se pueden ver los brazos en algunas MRI y puede generar ruido al momento de entrenar el modelo.  

## Target variable
La variable objetivo es la columna clase en el archivo csv. Tiene 3 valores diferentes, el intestino grueso, el delgado y el estómago. La columna de "segmentation" es la que sirve para la segmentación de cada uno de los organos. 


## Relationship between explanatory variables and target variable
La otra columna que aparece en el dataset es la del id de cada imágen. Lo que se realizó en el notebook de eda fue separar el path de cada imagen, así como el caso o paciente, el día y el número de imágen. Estas variables ayudarán mas adelante a poder analizar los resultados obtenidos para la segmentación. 

## Preprocesamiento del dataset
Para el preprocesamiento se crearon columnas con el nombre de cada uno de los organos que se pretenden identificar; Estomago, intestino largo y grueso y una columna para guardar el path de la máscara creada para cada organo.
Al tener dimensiones diferentes para cada imagen del dataset, se decidió normalizar el tamaño de estas a 256px x 256px. Además, se utilizó una función de cv2 para normalizar la imágen entre 0 y 255. Se guardaron las máscaras en una nueva ruta o path, y se muestran algunos ejemplos antes y después del preprocesamiento y la máscara creada para cada imágen. 
