# Data Report

This document contains the results from the exploratory data analysis.

## General summary of the data

The dataset is composed by 24,999 images of colonial american paints, portraying different religious scenes, landscapes and people. Files are in different formats like JPEG, JPG, PNG, TIF and different sizes. The datasest has been labeled manually un an Excel file, to identify diferente kind of typical human gestures.  

## Data quality summary

The model will be trained  on the base of a imagenet dataset Inception V3 that requieres a shape of (299,299,3) and doesn´t process TIF images. Then the dataset preprocessing involves recasting shape and extension of images.

## Target variable

The target label are the core 12 gestures defined with its ID are: 
'''
{34:"Entregar algo", 
49:"Llevar de la mano: cuidar débiles", 
55:"Mano abierta sobre corazón: afirmar testimonio",
208:"Mano derecha tres dedos: bedición, pedir silencio",
67:"mano extendida frente: bendecir", 
108:"Mano extendida pecho: aseverar",
201:"Manos atadas: sacrificio",
200:"Manos brazos cruzados pecho",
2:"Múltiples gestos",
4:"Oro:pedir misericordia",
5:"Ploro: condolerse",
73:"Señalar con dedo:mano, orden, traicionar"}
'''

## Variable ranking

12 variables have this number of observations:
'''
{34:"583", 
49:"262", 
55:"293",
208:"961",
67:"172", 
108:"623",
201:"498",
200:"834",
2:"1155",
4:"2063",
5:"509",
73:"454"}
'''


