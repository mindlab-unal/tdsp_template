# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each data, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided. 


## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| UW-Madison GI Tract Image Segmentation | La ubicación original de esta base de datos \n es de kaggle del siguiente link <a href = "https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation/data"> UW-Madison GI Tract Image Segmentation Data </a>  | El destino de esta base de datos varía dependiendo de cada persona \n del grupo. Será guardado en el computador personal | [data_acquisition.py](/scripts/data_acquisition/main.py) | [Resumen Dataset](/docs/data/data_dictionary.md)|


  
## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Dataset Procesado | El Dataset no fue incluido dentro del github \n por ser tan pesado. En el script \n mencionado posteriormente se muestran algunos ejemplos \n de imágenes segmentadas | [eda.ipynb](/docs/eda/eda.ipynb) | [Resultados EDA](/docs/data/data_summary.md)|


## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|


* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>

