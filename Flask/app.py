from gettext import install
import pickle
from flask import Flask, render_template , request
import pandas as pd
import numpy as np
model1 = pickle.load(open(r"C:\Users\HP\OneDrive\Desktop\maha\maha_model .pkl", 'rb'))
app=Flask(__name__)

@app.route('/')
def home( ):
    return render_template('index.html')
@app.route('/predict') # rendering the html template
def index() :
    return render_template('predict.html')
@app.route('/submit', methods=['GET','POST'])
def predict() :
    return render_template('watch_prediction.html')

    brand = request.form['Brand']
    model = request.form['Model']
    os = request.form['Operating System']  # Changed from 'Operating System' to 'os'
    connect = request.form['Connectivity']
    display_type = request.form['Display Type']  # Changed from 'Display_Type' to 'Display Type'
    display_size = request.form['Display Size']
    resolution = request.form['Resolution']
    water = request.form['Water Resistance']
    battery = request.form['Battery Life']
    gps = request.form['GPS']
    nfc = request.form['NFC']

    brand = request.form['Brand']
    if brand == 'Garmin':
          brand = 8
    if brand == 'Mobvoi' :
          brand = 18
    if brand == 'Fitbit':
          brand = 6
    if brand == 'Fossil':
          brand = 7
    if brand == 'Amazfit':
          brand = 0
    if brand == 'Samsung' :
          brand = 30
    if brand =='Huawei':
          brand = 10

    model = request.form['Model']
    if model == 'Hybrid HR' :
        model = 44
    if model =='Venu sq' :
        model = 196
    if model == 'MagicWatch 2':
        model = 56
    if model == 'Ticwatch Pro 3':
        model = 97
    if model == 'vapor x':
        model = 104
    if model == 'Z' :
        model = 132

    os = request.form['Operating System']
    if os == 'Wear os':
        os = 31
    if os =='Garmin os':
        os = 9
    if os == 'Lite os':
        os = 12

    connect = request.form['Connectivity']
    if connect == 'Bluetooth, wi-Fi':
        connect = 1
    if connect == 'Bluetooth, Wi-Fi, Cellular':
        connect = 2
    if connect == 'Bluetooth' :
        connect = 0
    if connect == 'Bluetooth, wi-Fi, GPS':
        connect = 3
    if connect == 'Bluetooth, wi-Fi, NFC':
        connect = 4

    display_type = request.form['Display Type']
    if display_type == 'AMOLED' :
        display_type = 0
    if display_type == 'LCD':
        display_type = 9

    # Assuming these are your features
    brand = 'Brand'
    model = 'Model'
    os = 'OS'
    connect = 'Connectivity'
    display_type = 'Display Type'
    display_size = 'Display Size'
    resolution = 'Resolution'
    water = 'Waterproof'
    heart = 'Heart Rate Monitor'  # Define the variable heart
    battery = 'Battery'
    gps = 'GPS'
    nfc = 'NFC'
    price = 'Price'



    prediction = model1.predict(pd.DataFrame([[brand,model,os,connect,display_type,display_size,resolution,water,heart,battery,gps,nfc,price]],
                               columns = ['Brand','Model','Operating System', 'Connectivity',
                                          'Display Type','Display Size', 'Resolution',
                                          'Water Resistance','Heart Rate Monitor','Battery Life',
                                          'GPS','NFC','Price']))


    prediction =np.round(prediction,2)
    return render_template("watch_prediction.html",prediction_text = "is {}".format(prediction))


if __name__ == '__main__':
    app.run()
