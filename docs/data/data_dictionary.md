# Data Dictionary

In this project I will be using a collection of images stored in Google Drive. Labels with gestures have been collected in a Excel file which served as a guide to reorganize the file tree, and having a folder for each label.
   
# Database Colonial_Images_labels

The original Dataset of 24,999 images is labeled with 253 different types of gestures, as show below.
First column named "Id" is the code/name of the image. Second column "id_gesto" is the code of the particular gesture identified in the picture. Third column "Gesto" is the string description of the the labeled gesture.

[Labels](https://drive.google.com/file/d/1ByhZrQSgKJGJYYDaSRcx0gqYvT8orAyB/view?usp=share_link)

A constraint of the Dataset is its non balanced by feature sampling. 10 out of 253 features or labels concentrate more than 60% of the images, and also contains a particular label which describes "no-gesture", so it could mislead the model training.

As a result of this analysis, the Dataset will be re-partitioned in a sample containing only a relevant group of features (labels), those containing more than 250 observations as show in the graphic below.  

[Labels_frequency](https://drive.google.com/file/d/1ByZjXQbPdH5yl2ECACSLx2FGWeCXKIyj/view?usp=share_link)

12 labels remain the core of the analysis and serve to train the Deep Learning model with fine tuning. A total of 8,690 images like the one displayed here:

[Image_sample](https://drive.google.com/file/d/1dWfhAQCa6WYkP2TxBCRXSVyg5KR15_1R/view?usp=share_link)