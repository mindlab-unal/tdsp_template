# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. 


## Raw Data Sources

| Dataset Name | Original Location   | Destination Location | Link to Report |
| ---:| ---: | ---: | ---: |
| Colonial_Images| The original dataset is the result of a collaborative historical project named Arca, of the Universidad de los Andes-Colombia  | Original Dataset is published in the book 'Los ingenios del pincel' | [book](https://losingeniosdelpincel.uniandes.edu.co/arca/) |

* Dataset Colonial_Images summary. All paintings are labeled with their titles, main characters/categories, identified visual stories, authorship, place and probable dates of production, current location, among others. 

## Processed Data
| Processed  | Input Dataset  | Data Processing Tools/Scripts | 
| ---:| ---: | ---: | 
| Processed Colonial_Images_labels | Excel file with gestures labels | [labels](https://drive.google.com/file/d/1ByhZrQSgKJGJYYDaSRcx0gqYvT8orAyB/view?usp=share_link)| 
* Processed Colonial_Images_labels summary. 253 different types of gestures have been labeled to each image.


## Feature Sets

| Feature Set Name | Input Dataset(s)  | Feature Script  |
| ---:| ---: | ---: |
| Feature labels | [Colonial_Images_labels](https://drive.google.com/file/d/1ByhZrQSgKJGJYYDaSRcx0gqYvT8orAyB/view?usp=share_link) | [Python script](```# Select labels with frequency higher than 250 and drop feature 255 code for "non gesture" etiquetas_1=list(y_1[X_1>=250]) etiquetas_1.remove(255)```|


* Feature labels summary. Dataset will be re-partitioned in a sample containing only a relevant group of features (labels), those containing more than 250 observations, except for the 'non-gesture' label. A total of 8,690 images for 12 labels resulted.

