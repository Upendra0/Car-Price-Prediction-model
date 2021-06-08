from flask import Flask, render_template, request
import jsonify
import numpy as np
import sklearn
from joblib import load

model = load("model.pkl")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)