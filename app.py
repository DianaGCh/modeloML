from crypt import methods
from flask import Flask
from pyspark import F
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'MODELO DE PREDICCION CON MACHINE LEARNING'

@app.route("/predecir", methods=["POST"])
def predecir():
    return 'Predicciones page'

if __name__ == "__main__":
    app.run()