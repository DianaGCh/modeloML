from flask import Flask , render_template, request
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    #return 'MODELO DE PREDICCION CON MACHINE LEARNING'
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    item = [x for x in request.form.values()]
    data = []

    print(item)

    
    if item[0] == 'basico':
        data.append(0)
    else:
        data.append(1)

    data.append(int(item[1]))

    if item[2] == 'solo':
        data.append(0)
    else:
        data.append(1)
    
    data.append(int(item[3]))
    data.append(int(item[4]))
    data.append(int(item[5]))
    data.append(int(item[6]))
    data.append(int(item[7]))
    data.append(int(item[8]))

    dataNumpy = np.array(data)
    dataNumpy = dataNumpy.reshape(1,-1)
    
    filename = './modelo_entrenado.pkl'
    model = pickle.load(open(filename,"rb"))

    prediccion=model.predict(dataNumpy)

    print(prediccion[0])
    return 'Los datos ingresados corresponden a un cliente de nivel: {0}\n\n'.format(prediccion[0])

    #return render_template('index.html', prediction_text='The Insurance cost will be   $ {}'.format(output))

if __name__ == "__main__":
    app.run()