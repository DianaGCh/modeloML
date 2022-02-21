from crypt import methods
from flask import Flask , render_template
#from pyspark import F
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    #return 'MODELO DE PREDICCION CON MACHINE LEARNING'
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    item = [x for x in request.form.values()]
    data = []

    data.append(int(item[0]))
    
    
    if item[1] == 'Education':
        data.append(0)
        data.append(1)
    else:
        data.append(1)
        data.append(0)

    if item[2] == 'Relation':
        data.append(1)
        data.append(0)
    else:
        data.append(0)
        data.append(1)
    
    clf=joblib.load('Modelo_Entrenado.pkl')
    prediccion=clf.predict(data)
    return 'los datos ingresados corresponden a un cliente de nivel: {0}\n\n'.format(prediccion)

    return render_template('index.html', prediction_text='The Insurance cost will be   $ {}'.format(output))

if __name__ == "__main__":
    app.run()