# Data Dictionary

# UW-Madison GI Tract Image Segmentation

Esta base de datos consiste en múltiples resonancias magnéticas de pacientes tratados en el Carbon Cancer Center de la universidad de Wisconsin Madison (UW-Madison). 
Las resonancias son de pacientes que fueron tratados con radioterapia desde el 2015 por tener cancer en el estomago u organos cercanos. A estos pacientes se les realizó
de 1 a 5 resonancias magneticas en diferentes días para ver la evolución del tumor y de los diferentes organos con la radioterapia. 

Dentro de la base de datos hay aproximdamente 38500 imágenes organizadas de la siguiente manera.

![DataDiagram](/docs/data/Diagrama%20Datos.jpg)

Cada caso es un paciente diferente y hay 85 en total. En cada carpeta de cada paciente hay una o más carpetas de los días que le hicieron escaneos a cada paciente, desde el día 0 hasta el día N de tratamiento. Y dentro de cada carpeta de cada día hay 100 o más imágenes de la resonancia realizada ese día. Cabe aclarar que hay algunas imágenes que están completamente negras pues es como el inicio de la resonancia y no hay un detalle a observar claramente durante este periodo.

Aparte de las imagenes que se utilizaran para entrenar el modelo, hay un archivo csv llamado train, el cual consiste en 3 columnas; la primera columna es un ID que identifica cada imágen dentro de la base de datos, otra columna con la etiqueta de cada imagen, si es estomago grueso, delgado o el y finalmente una columna de segmentación. Esta columna es un RLE-codificado con los valores de segmentación en la imagen identificada en cada fila. 

## Tabla 1


| column | type | description |
| --- | --- | --- |
| ID | str | case123_day20_slice_0001: Paciente o caso 123, el día # 20 desde que empezó la radioteraía, y es el primer escaneo que va a hacer|
| class | str | large bowel, stomach or small bowel |
|segmentation | str | (23877 13 24139 18 24405 19 24671 20 24936 21 25200 24 25465 27 25730 29 25995 31 26260 32 26525 34 26790 36 27055 37 27320 39 27584 41 27848 44 28110 48 28375 49 28639 51 28902 54 29166 56 29430 57 29694 58 29960 58 30225 58 30492 56 30758 54 31024 52 31291 50 31558 49 31825 47 32020 5 32091 46 32285 7 32358 45 32550 8 32625 7 32634 34 32816 8 32902 31 33082 9 33169 30 33348 11 33436 29 33614 12 33703 27 33881 12 33974 21 34147 13 34242 19 34414 12 34509 18 34680 13 34775 18 34948 10 35042 17 35216 8 35308 18 35483 6 35575 16 35752 1 35843 14 36116 6 36384 3) RLE-codificado | 
