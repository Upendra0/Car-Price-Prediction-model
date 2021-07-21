from flask import Flask, render_template, request, jsonify
import sklearn
from joblib import load

model = load("model.pkl")
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    This renders the home page of our application where user has to fill the form
    to predict the selling price.
    """
    return render_template("index.html")


@app.route("/predict",methods=["POST", "GET"])
def predict():
    """
    This function redirect the user to home page if user has not send the form data
    else it extract the data from form field and run the machine learning algorithm
    to predict the selling price of the car.
    """
    if request.method == "POST":
        model = load("model.pkl")
        year = int(request.form["year"])
        present_price = int(request.form["present_price"])
        km_driven = int(request.form["km_driven"])
        n_owner = int(request.form["owner"])
        fuel_type_petrol = fuel_type_diesel = 0
        if(request.form["fuel_type"] == "Petrol"):
            fuel_type_petrol = 1
        elif(request.form["fuel_type"] == "Diesel"):
            fuel_type_diesel = 1
        seller_type_indvidual = 0
        if(request.form["seller_type"] == "Individual"):
            seller_type_indvidual = 1
        transmission_mannual = 0
        if(request.form["gear_type"] == "mannual"):
            transmission_mannual = 1
        x = [[year, present_price, km_driven, n_owner, fuel_type_diesel,
             fuel_type_petrol, seller_type_indvidual, transmission_mannual]]
        y = model.predict(x)[0]
        y = float(y)
        y = round(y,2)
        return render_template("prediction.html", price=y)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
