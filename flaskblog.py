import io 
import base64
from flask import Flask, escape, request , render_template, url_for,Response,make_response
from flask.helpers import send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
from matplotlib.figure import Figure
import random

# Plot evaluation 

app = Flask(__name__)

@app.route('/tmpplot/')
def plot():
    fig, ax = plt.subplots()
    plt.plot([1,2,3,4])
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype ='image/png')

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return render_template('home.html')

@app.route('/about')
def about():
    name = request.args.get("name", "World")
    return f'<h1>About Page</h1>'

if __name__ == '__main__':
    app.run(debug = True)
