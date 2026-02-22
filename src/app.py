from flask import Flask, request, render_template
import pickle
import os


app = Flask(__name__)

model = None



def load_model():
    global model

    if model is None:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(BASE_DIR, "air_quality_model.pkl")

        model = pickle.load(open(model_path, "rb"))

    return model


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=["POST"])
def predict():

    # Obtener datos del formulario   CO = float(request.form["CO"])
    NO2 = float(request.form["NO2"])
    SO2 = float(request.form["SO2"])
    O3 = float(request.form["O3"])
    PM2_5 = float(request.form["PM2_5"])
    PM10 = float(request.form["PM10"])

    features = [[CO, NO2, SO2, O3, PM2_5, PM10]]

    model = load_model()

    prediction = model.predict(features)[0]

    result = "Unhealthy" if prediction == 1 else "Safe"

    return render_template(
        "index.html",
        prediction=result
    )