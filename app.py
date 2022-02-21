from crypt import methods
from flask import Flask
#from pyspark import F
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#@app.route('/')
#def home():
  #  return 'MODELO DE PREDICCION CON MACHINE LEARNING'

@app.route('/',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    item = [x for x in request.form.values()]
    data = []

    data.append(int(item[0]))
    if item[1] == 'Male':
        data.append(0)
        data.append(1)
    else:
        data.append(1)
        data.append(0)

    if item[2] == 'No':
        data.append(1)
        data.append(0)
    else:
        data.append(0)
        data.append(1)
    
    prediction = model.predict([data])

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The Insurance cost will be   $ {}'.format(output))

if __name__ == "__main__":
    app.run()