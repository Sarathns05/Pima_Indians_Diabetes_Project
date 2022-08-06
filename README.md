
Pima Indians Diabetes Project
-------------------------------
This is an end-to-end Machine Learning project to predict whether the person has Diabetes or not.

Overview
------------

In this project, the objective is to predict whether the person has Diabetes or not based on various features suach as

     
        1: Pregnancies: Number of times pregnant

        2: Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test

        3: BloodPressure: Diastolic blood pressure (mm Hg)

        4: SkinThickness: Triceps skinfold thickness (mm)

        5: Insulin: 2-Hour serum insulin (mu U/ml)

        6: BMI: Body mass index (weight in kg/(height in m)²)

        7: DiabetesPedigreeFunction: Diabetes pedigree function

        8: Age: Age (years)


Data Source
--------------
https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database. 


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
* See the deployed application here - https://diabetesfinder.herokuapp.com/
