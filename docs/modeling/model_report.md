# Final Model Report
_Report describing the final model to be delivered - typically comprised of one or more of the models built during the life of the project_

## Analytic Approach
* What is target definition
  * Lo que se pretende obtener después de entrenar el modelo son máscaras o la segmentación de una imágen, que es capaz de diferenciar entre estomago, intestino grueso ó el delgado. Habiendo hecho la segmentación se pretende identificar si hay tumores o no en un paciente, y así poder tratarlo. Esto se realiza, ya que después de una resonancia magnética, no es posible diferenciar claramente si un paciente tiene o no tumor, y si el tratamiento ha o no ha servido. 
* What are inputs (description)
  * Las entradas al modelo fueron las 115 mil imágenes, cada una normalizada y todas con el mismo tamaño. 
* What kind of model was built?
  * El modelo creado es uno secuencial de generación - discriminador con múltiples capas convolucionales y convolucionales transpuestas. 

## Solution Description
* Simple solution architecture (Data sources, solution components, data flow)
  * 
* What is output?
  * La salida del modelo es una imágen que muestra con colores donde está ubicado el tumor de cada paciente. 

## Data
* Source
  * El origen de los datos es de una competencia en kaggle llamada <a href = "https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation/data"> UW-Madison GI Tract Image Segmentation Data </a>. 
* Data Schema
  * [Diagrama de Datos](/docs/data/Diagrama%20Datos.jpg)
* Sampling
  * Los datos se muestraron en el notebook de [EDA](/scripts/eda/eda.ipynb) aleatoriamente. Allí se muestran ciertas imágenes, con colores y con máscaras ya creadas- 
* Selection (dates, segments)
  * Para entrenar el modelo se hizo train_test_split y se dividió 80/20, 80% para entrenar el modelo y 20% para validar el modelo. 
* Stats (counts)
  * La cantidad de imágenes que se utilizaron para meter al modelo fueron 49770, las cuales erán las que estaban correctamente segmentadas en un principio. 

## Features
* List of raw and derived features 
* Importance ranking.
  * No existe un ranking de importancia

## Algorithm
* Description or images of data flow graph
  * El flujo del algoritmo utilizado se encuentra [acá](/scripts/training/model.png). El algoritmo se divide en tres partes, la primera parte es un downsample que contiene 8 capas convolucionales 2D, cada una con diferente cantidad de filtros. Después sigue un upsample, que es lo contrario a la etapa anterior, esta parte está compuesta por múltiples capas 2D transpuestas, 8 especificamente. En total, la cantidad de parámetros es 54,425,923. 
  La última parte consiste en un discriminador con 4 capas convolucionales 2D transpuestas y una final 2D normal. De ahí salen otros 2,786,883 parámetros
* What learner(s) were used?
  * Se utilizó el optimizador Adam, y se creó un discriminador y se va calculando el gradiente entre la perdida del discriminador y las variables entrenables en las capas discriminantes. Estos grádientes se aplican a las capas generadoras. 
  
* Learner hyper-parameters
  * Los hiper parámetros que se variaron fueron la cantidad de filtros en cada capa, y las funciones de activación, pues se utilizaron Leaky ReLu y ReLu. 

## Results
* ROC/Lift charts, AUC, R^2, MAPE as appropriate
  * 
* Performance graphs for parameters sweeps if applicable
