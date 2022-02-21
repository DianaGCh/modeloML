from crypt import methods
from flask import Flask
#from pyspark import F
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'MODELO DE PREDICCION CON MACHINE LEARNING'


if __name__ == "__main__":
    app.run()