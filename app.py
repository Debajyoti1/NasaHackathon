from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from random import sample
app = Flask(__name__)
app.secret_key='Hellothere'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/data')
def data():
    return jsonify({'results' : sample(range(1,50), 7)})
if __name__ == '__main__':
    app.run(debug=True)