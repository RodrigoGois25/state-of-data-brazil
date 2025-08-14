import os

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Carregando os modelos
caminho_modelo = os.path.join("..", "models", "modelo_cargo_pipeline.joblib")
caminho_encoder = os.path.join("..", "models", "label_encoder_cargo.joblib")
model_pipeline = joblib.load(caminho_modelo)
label_encoder = joblib.load(caminho_encoder)
print("Modelo e Encoder carregados com sucesso.")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Receber os dados da requisição em formato JSON
    json_data = request.get_json()

    # --- INÍCIO DA NOVA DEPURAÇÃO ---
    print("\n--- DADOS RECEBIDOS DO N8N ---")
    print(json_data)
    print("-----------------------------\n")
    # --- FIM DA NOVA DEPURAÇÃO ---

    # Se não receber nenhum dado JSON, retorna um erro claro
    if json_data is None:
        return jsonify(
            {"erro": "Nenhum dado JSON recebido no corpo da requisição."}
        ), 400

    # Converter os dados JSON em um DataFrame do Pandas
    dados_usuario = pd.DataFrame(json_data, index=[0])

    try:
        # Usar o pipeline para fazer a predição
        predicao_numerica = model_pipeline.predict(dados_usuario)

        # Converter a predição numérica de volta para o nome do cargo (texto)
        cargo_predito = label_encoder.inverse_transform(predicao_numerica)

        # Retornar o resultado como JSON
        return jsonify({"cargo_predito": cargo_predito[0]})

    except Exception as e:
        # Em caso de erro, retornar uma mensagem de erro
        return jsonify({"erro": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
