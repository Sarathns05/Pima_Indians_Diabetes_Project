
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
- [Kaggle-Pima-Indian-Diabetes-Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database.)


Technology and tools use
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

#### STEP 1: Data Preparation and model building

In this step, explore the data, do the required pre-processing and try various Machine Learning models

#### STEP 2: Building the app using Flask and HTML

Here, fetch the best-performing model from step 1 and build a web app using Flask and HTML.

#### STEP 3: Deploying the app using Heroku

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

  #### PAIRPLOT :
 
![Pairplot(PimaIndianDiabetes)](https://user-images.githubusercontent.com/108679625/197686035-1626f601-aedb-40bd-8a8f-e1305808e4a0.png)

* Check the number of zeros in each independent variables and done the outlier treatment using 'Skin Thickness' variable.
* Replace the zeros using the median value of dataset.
* Check the countinuos columns in dataset and it cap with standard deviation

#### TRAIN TEST SPLIT :
 * Spliting the dataset into X and y.
 * 70% for trainning and 30% for testing.
![Screenshot from 2022-10-25 10-37-45](https://user-images.githubusercontent.com/108679625/197687744-a81f1cd7-676d-4dae-8096-b726bbd87d01.png)

#### SCALE DOWNN :
 * It is done using StandardScaler function
 * create pickle file of scale down using joblib
![Screenshot from 2022-10-25 10-37-45(1)](https://user-images.githubusercontent.com/108679625/197687909-ecd9eab4-86cf-4495-8ce8-77daa3508ac4.png)

 #### MODEL BUILDING :
  * Apply all classification algorithms
  * check the accuracy score of trainning and testing
![Screenshot from 2022-10-25 10-46-33](https://user-images.githubusercontent.com/108679625/197688784-c3d5d65e-f5fb-4259-90fe-bd9a5c56d272.png)
![Screenshot from 2022-10-25 10-46-33(1)](https://user-images.githubusercontent.com/108679625/197688939-764cfa79-ae5b-49f7-a996-3d0be998e32f.png)
![Screenshot from 2022-10-25 10-51-01](https://user-images.githubusercontent.com/108679625/197689274-d1f91996-8c76-4207-9395-b614406ed441.png)

#### HYPERPARAMETER TUNNING :
 * Hyperparameter tunning done in all algorithms to find best model
 * SVC gives the best accuracy
 * Making the best model SVC and saving it as pickle file using joblib
![Screenshot from 2022-10-25 10-57-45](https://user-images.githubusercontent.com/108679625/197690253-3a4efe33-844f-4cf7-bebc-a5d321c68d62.png)
![Screenshot from 2022-10-25 10-59-56](https://user-images.githubusercontent.com/108679625/197690580-b7df9bc1-d407-4d2f-a243-1572542fa96c.png)

  
STEP 2: Building the app using Flask and HTML
-----------------------------------------------
 * Create a new file app.py.
 * Import the flask module, and create a Flask app by instantiating the Flask class
 * Import the saved pre-processer element and the model.
 * Define the route that will render the index.html webpage (created using HTML). This file has CSS running and background for the look and feel.
 * Define the predict/ route and a function corresponding to it that will accept the different values for the inputs and return the predictions using the
   SVM model
![Sreenshot from 2022-10-25 11-07-09](https://user-images.githubusercontent.com/108679625/197691443-b6a7c3c4-19fe-40ec-a54b-0c24847dec1b.png)




STEP 3: Deploying the app using Heroku
---------------------------------------

* The web application is built using python library -> Flask and Web Programming languages -> HTML, CSS
* The entire application is finally deployed on Heroku by adding - Procfile (informs Heroku that which application is to be run first), Requirements         (notifies Heroku about the libraries that needs to be installed before deploying or running our application)
* See the deployed application [here](https://diabetesfinder.herokuapp.com/).

![appUI](https://user-images.githubusercontent.com/108679625/184126797-82acbee0-058a-4224-a6a7-bb2363a68a3b.png)

![appUI2](https://user-images.githubusercontent.com/108679625/184127353-95767649-f3e6-4d7e-9ac0-c5a7bc93fc4f.png)


