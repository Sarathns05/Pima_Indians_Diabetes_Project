#import relevant libraries for flask, html rendering and loading the ML model 
from flask import Flask,request, url_for, redirect, render_template 
import pickle 
import pandas as pd
import joblib

app = Flask(__name__) 

model= joblib.load(open("model.pkl")) 
scale = joblib.load(open("scaled.pkl")) 

@app.route("/") 
def hello_world():
    return render_template('index.html')   

if __name__ == '__main__':
    app.run(debug=True)   