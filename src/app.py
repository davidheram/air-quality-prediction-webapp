from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("air_quality_model.pkl", "rb"))

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict(): 
    CO = float(request.form["CO"])
    NO2 = float(request.form["NO2"])
    SO2 = float(request.form["SO2"])
    O3 = float(request.form["O3"])
    PM2_5 = float(request.form["PM2_5"])
    PM10 = float(request.form["PM10"])

    features = [[CO, NO2, SO2, O3, PM2_5, PM10]]

    prediction = model.predict(features)[0]

    result = "Unhealthy" if prediction == 1 else "Safe"

    return render_template(
        "index.html",
        prediction=result
    )


if __name__=="__main__":
    app.run(debug=True)