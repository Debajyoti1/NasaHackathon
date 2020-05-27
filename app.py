from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from random import sample
import pandas as pd

dataframe=pd.read_csv("dataset.csv")

area=list(dataframe['Area'])
density=list(dataframe['Density'])
active=list(dataframe['Active'])



app = Flask(__name__)
app.secret_key='Hellothere'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/popvsconf')
def popvsconf(df=dataframe):
    df=df.sort_values(by='Population')
    confirmed=list(df['Confirmed'])
    population=list(df['Population'])
    confirmed.remove(31972)
    population.remove(3145966)
    return jsonify({'confirmed' : confirmed,'population' : population})


@app.route('/areavsconf')
def areavsconf(df=dataframe):
    df=df.sort_values(by='Area')
    confirmed=list(df['Confirmed'])
    area=list(map(int,(df['Area'])))
    return jsonify({'confirmed' : confirmed,'area' : area})

@app.route('/denvsconf')
def denvsconf(df=dataframe):
    df=df.sort_values(by='Density')
    confirmed=list(df['Confirmed'])
    density=list(map(int,(df['Density'])))
    return jsonify({'confirmed' : confirmed,'density' : density})

@app.route('/actvsconf')
def actvsconf(df=dataframe):
    df=df.sort_values(by='Active')
    confirmed=list(df['Confirmed'])
    active=list(df['Active'])
    return jsonify({'confirmed' : confirmed,'active' : active})


if __name__ == '__main__':
    app.run(debug=True)