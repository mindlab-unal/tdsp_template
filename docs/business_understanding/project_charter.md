# Project Charter

## Business background

* Who is the client, what business domain the client is in?
The original Dataset is made up of 24,999 images in JPG, JPEG, PNG, TIF files of American colonial paintings, labeled with the object and the main gesture identified in each one. This Dataset is the result of the research project [Arca - Los Ingenios del Pincel](https://losingeniosdelpincel.uniandes.edu.co) coordinated by Dr. Jaime Humberto Borja, professor of History at the Universidad de los Andes - Bogotá.

* What business problems are we trying to address?
The project has already completed its first phase of labeling all the paintings, with their titles, main characters/categories, identified visual stories, authorship, place and probable dates of production, current location, among others. The collection has been indexed on a web page for free consultation.
The second phase focuses on studying the gestures and physiognomies of the human characters represented in the collection, for which 253 different types of gestures labeled and 153 relevant objects within the scenes. Studying gestures in art will allow social scientists to advance in identifying patterns and generalities/particularities of human gestural language over time and in different cultures.

## Scope
* What data science solutions are we trying to build?
A Deep Learning model with Fine-Tuning techniques will be developed, using the curated original Dataset of American Colonial Paintings, with gestures labeled to train the gesture and object recognition function in pictorial representations.

* What will we do?
We will use a Inception V3 model from Imagenet and use Fine-Tuning with the Dataset of American Colonial Painting 

* How is it going to be consumed by the customer?
The trained model will be deployed as an API to consume by a Webservice. The final user could use ir to recognize same gesture patterns in other painting samples.

## Personnel
* Who are on this project:
	* Laura Manrique - Full stack Data scientist 

	* Client:
		* Bitlical. Company's web site
		* Dr. Jaime Humberto Borja - Head of research - Colonial Painting Project Arca- Universidad de los Andes - Bogotá
	
## Metrics
* What are the qualitative objectives? Provide a model to identify through paintings how colonial gestures patterns have change over different regions and time. 
* What is a quantifiable metric? Achieve an accuracy metrics superior to 60%
* What is the baseline (current) value of the metric? There is not known model for this particular task

## Plan
* Phases (milestones): 1. Understanding dataset 2. Modelling best gestures patterns to set task 3. Retrieving data 4.Training model 5.Measuring results 6.Creating API 7. Deploying on web site

## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (Files stored in a Google Drive repository: 24,999 images in jpeg, jpg, png, tif) 

* What tools and data storage/analytics resources will be used in the solution,
  * Python for feature construction, aggregation and sampling

* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? 
  * The customer will use the model results to make decisions by uploading new images and using the trained model to find which colonial gesture is present into the drawing.

## Communication
* There will be Weekly meetings to update status.
