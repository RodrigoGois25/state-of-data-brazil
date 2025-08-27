import pandas as pd
from flask import Flask, jsonify, render_template, request
from joblib import load

app = Flask(__name__)

# Carregando Modelos e Encoders
try:
    model = load("../models/neural_network_model.joblib")
    labels = load("../models/label_encoder.joblib")
    print(
        """Modelo e Encoder Carregados com Sucesso!\n
        São Esperadas as Colunas:""",
        model.feature_names_in_,
    )
except Exception as error:
    print(error)
    raise


# Rota Home
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# Rota de Predição
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Converte a Requisição JSON em DataFrame
        data = pd.DataFrame(request.get_json(), index=[0])
        print(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    try:
        numeric_prediction = model.predict(data)
        label_prediction = labels.inverse_transform(numeric_prediction)
        return jsonify({"predicted_job": label_prediction[0].title()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
