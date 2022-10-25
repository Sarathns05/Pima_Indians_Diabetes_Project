
# End To End Diabetes Prediction Application Using Machine Learning


Dataset Details
------------

   * Pregnancies: Number of times pregnant
   * Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
   * BloodPressure: Diastolic blood pressure (mm Hg)
   * SkinThickness: Triceps skinfold thickness (mm)
   * Insulin: 2-Hour serum insulin (mu U/ml)
   * BMI: Body mass index (weight in kg/(height in m)²)
   * DiabetesPedigreeFunction: Diabetes pedigree function
   * Age: Age (years)



Data Source
--------------
https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database.


Technology and tools used
-------------------------

* Python
* Numpy and Pandas for data cleaning
* Sklearn for model building
* Google colab as IDE
* Python flask for http server
* HTML/CSS for UI
* Heroku for deployement



Overview
----------

STEP 1: Data Preparation and model building

In this step, explore the data, do the required pre-processing and try various Machine Learning models

STEP 2: Building the app using Flask and HTML

Here, fetch the best-performing model from step 1 and build a web app using Flask and HTML.

STEP 3: Deploying the app using Heroku

In the end deploy the working app through Heroku for the world to use our product.
  


STEP 1 : Data Preparation and Model Building
----------------------------------------------

Importing the required Libraries and Loading the Dataset
![Screenshot from 2022-08-12 09-35-45](https://user-images.githubusercontent.com/108679625/197683462-cde430af-9a84-4a17-b348-cb96b78c56c9.png)

#### EDA(Exploratory Data Analysis) :
  *  Analy the target variable (Outcome)
  *  Check the unique values, count and correlation in target variables and also plot it.
  *  After done the value count. I understand the dataset is imbalance
  *  Check the dataset information such as shape, info, describe, identify missing value using isna().
  *  plot the heatmap using correlation in input dataset.

![correlation(PimaIndianDiabetes)](https://user-images.githubusercontent.com/108679625/197685682-c06780ed-3aba-4db0-af25-03035626dd18.png)

  ##### PAIRPLOT :
 
![Pairplot(PimaIndianDiabetes)](https://user-images.githubusercontent.com/108679625/197686035-1626f601-aedb-40bd-8a8f-e1305808e4a0.png)

  

Model Deployment
--------------------

* The web application is built using python library -> Flask and Web Programming languages -> HTML, CSS
* The entire application is finally deployed on Heroku by adding - Procfile (informs Heroku that which application is to be run first), Requirements         (notifies Heroku about the libraries that needs to be installed before deploying or running our application)
* See the deployed application [here](https://diabetesfinder.herokuapp.com/).


![appUI](https://user-images.githubusercontent.com/108679625/184126797-82acbee0-058a-4224-a6a7-bb2363a68a3b.png)

![appUI2](https://user-images.githubusercontent.com/108679625/184127353-95767649-f3e6-4d7e-9ac0-c5a7bc93fc4f.png)


