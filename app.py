import numpy as np
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

#penting
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features=None
    int_features= [x for x in request.form.values()]


    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(   int_features ))
