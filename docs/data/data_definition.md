# Data and Feature Definitions

## Raw Data Sources

| Dataset Name | Original Location   | <p align="center"> Destination Location </p> | <p align="center"> Data Movement Tools / Scripts </p> | <p align="center"> Link to Report </p> |
| ---:| ---: | ---: | ---: | -----: |
| <p align="center"> UW-Madison GI Tract Image Segmentation </p> | <p align="center"> La ubicación original de esta base de datos es de kaggle del siguiente link <a href = "https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation/data"> UW-Madison GI Tract Image Segmentation Data </a> </p> | <p align="center"> El destino de esta base de datos varía dependiendo de cada persona del grupo. Será guardado en el computador personal  </p>| <p align="center"> [Script Adquisición de datos.py](/scripts/data_acquisition/main.ipynb) </p>| <p align="center"> [Resumen Dataset](/docs/data/data_dictionary.md) </p>|


  
## Processed Data
| <p align="center"> Processed Dataset Name </p> | <p align="center"> Input Dataset(s) </p> | <p align="center"> Data Processing Tools/Scripts </p> | <p align="center"> Link to Report </p> |
| ---:| ---: | ---: | ---: | 
| <p align="center"> Image Segmentation Processed </p> | <p align="center"> El Dataset no fue incluido dentro del github por ser tan pesado. En el script mencionado posteriormente se muestran algunos ejemplos de imágenes segmentadas </p> | <p align="center"> [Exploratory Data Analysis Notebook](/scripts/eda/eda.ipynb) </p> | <p align="center"> [Resultados EDA](/docs/data/data_summary.md) </p> |
| <p align="center"> Preprocessing Data </p> | <p align="center"> El Dataset de entrada es el que se obtiene despues de realizar el EDA. A esos datos se les realiza preprocesamiento, el cual consiste en normalizar las imágenes. En el link mencionado en la columna Link to Report se explica detalladamente </p> | <p align="center"> [Preprocessing Notebook](/scripts/preprocessing/preprocessing.ipynb) </p> | <p align="center"> [Resultados Preprocesamiento](/docs/data/data_summary.md) </p> |

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>



