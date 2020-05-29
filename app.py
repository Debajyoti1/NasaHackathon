from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from random import sample
import pandas as pd

dataframe=pd.read_csv("dataset.csv")
dataframe=dataframe.sort_values(by='Confirmed')
for _ in range(6):
    dataframe.drop(dataframe.index[-1], inplace= True)
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

@app.route('/retvsconf')
def retvsconf(df=dataframe):
    df=df.sort_values(by='Retail')
    confirmed=list(df['Confirmed'])
    retail=list(df['Retail'])
    return jsonify({'confirmed' : confirmed,'retail' : retail})

@app.route('/grovsconf')
def grovsconf(df=dataframe):
    df=df.sort_values(by='Grocery')
    confirmed=list(df['Confirmed'])
    grocery=list(df['Grocery'])
    return jsonify({'confirmed' : confirmed,'grocery' : grocery})

@app.route('/parvsconf')
def parvsconf(df=dataframe):
    df=df.sort_values(by='Parks')
    confirmed=list(df['Confirmed'])
    parks=list(df['Parks'])
    return jsonify({'confirmed' : confirmed,'parks' : parks})

@app.route('/stavsconf')
def stavsconf(df=dataframe):
    df=df.sort_values(by='Stations')
    confirmed=list(df['Confirmed'])
    stations=list(df['Stations'])
    return jsonify({'confirmed' : confirmed,'stations' : stations})

@app.route('/worvsconf')
def worvsconf(df=dataframe):
    df=df.sort_values(by='Workplaces')
    confirmed=list(df['Confirmed'])
    workplaces=list(df['Workplaces'])
    return jsonify({'confirmed' : confirmed,'workplaces' : workplaces})

@app.route('/resvsconf')
def resvsconf(df=dataframe):
    df=df.sort_values(by='Residential')
    confirmed=list(df['Confirmed'])
    residential=list(df['Residential'])
    return jsonify({'confirmed' : confirmed,'residential' : residential})

if __name__ == '__main__':
    app.run(debug=True)