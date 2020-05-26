from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from random import sample
import pandas as pd

dataframe=pd.read_csv("dataset.csv")
confirmed=list(dataframe['Confirmed'])
population=list(dataframe['Population'])
area=list(dataframe['Area'])
density=list(dataframe['Density'])
active=list(dataframe['Active'])


app = Flask(__name__)
app.secret_key='Hellothere'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirmedj')
def confirmedj():
    return jsonify({'confirmed' : confirmed})


@app.route('/populationj')
def populationj():
    return jsonify({'population' : population})

@app.route('/areaj')
def areaj():
    return jsonify({'area' : area})

@app.route('/densityj')
def densityj():
    return jsonify({'density' : density})

@app.route('/activej')
def activej():
    return jsonify({'active' : active})

if __name__ == '__main__':
    app.run(debug=True)