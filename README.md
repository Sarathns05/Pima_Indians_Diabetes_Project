
Pima Indians Diabetes Project
-------------------------------

![appUI](https://user-images.githubusercontent.com/108679625/183301198-6cbcceb5-e37d-4ceb-b3d1-aa6b3a474066.png)

This is an end-to-end Machine Learning project to predict whether the person has Diabetes or not.

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

Learning Objective
-------------------

The following points were the objective of the project.(The main intention was to create an end-to-end ML project.)

  * Data gathering
  * Descriptive Analysis
  * Data Visualizations
  * Data Preprocessing
  * Data Modelling
  * Model Evaluation
  * Model Deployment
  
Overview
----------

Step 1: Data Preparation and model building

       In this step, explore the data, do the required pre-processing and try various Machine Learning models

Step 2: Building the app using Flask and HTML

        Here, fetch the best-performing model from step 1 and build a web app using Flask and HTML.

Step 3: Deploying the app using Heroku

        In the end deploy the working app through Heroku for the world to use our product.
  

Technology and tools used
-------------------------

* Python
* Numpy and Pandas for data cleaning
* Matplotlib for visualisation
* Sklearn for model building
* Google colab as IDE
* Python flask for http server
* HTML/CSS for UI
* Heroku for deployement

Model Deployment
--------------------

* The web application is built using python library -> Flask and Web Programming languages -> HTML, CSS
* The entire application is finally deployed on Heroku by adding - Procfile (informs Heroku that which application is to be run first), Requirements         (notifies Heroku about the libraries that needs to be installed before deploying or running our application)
* See the deployed application https://diabetesfinder.herokuapp.com/

