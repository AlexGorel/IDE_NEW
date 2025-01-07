#!pip install flask

#from flask import Flask
#app = Flask(__name__)
#@app.route('/hello')
#def hello_func():
    #return 'hello!'
#if __name__ == '__main__':
    #app.run('localhost', 5000)

#from flask import Flask
#app = Flask(__name__)
#@app.route('/')
#def index():
    #return 'Test message. The server is running'
#if __name__ == '__main__':
    #app.run('localhost', 5000)

#from flask import Flask,request
#app = Flask(__name__)
#@app.route('/hello')
#def hello_func():
    #name=request.args.get('name')
    #return f'hello {name}!'
#if __name__ == '__main__':
    #app.run('localhost', 5000)

#from flask import Flask
#import datetime
#app = Flask(__name__)
#@app.route('/time')
#def current_time():
    #return {'time': datetime.datetime.now()}
#if __name__ == '__main__':
    #app.run('localhost', 5000)



#from flask import Flask,request
#app = Flask(__name__)
#@app.route('/hello')
#def hello_func():
    #name=request.args.get('name')
    #return f'hello {name}!'
#if __name__ == '__main__':
    #app.run('localhost', 5000)


#from flask import Flask,request,jsonify
#app = Flask(__name__)
#@app.route('/add', methods=['POST'])
#def add():
    #num = request.json.get('num')
    #if num>10:
        #return 'too much',400
    #return jsonify ({
        #'result':num+1
    #})
#if __name__ == '__main__':
    #app.run('localhost',5000)

#import requests

#if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    #r = requests.post('http://localhost:5000/add', json={'num': 15})
    # выводим статус запроса
    #print(r.status_code)
    # реализуем обработку результата
    #if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        #print(r.json()['result'])
    #else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        #print(r.text)

from flask import Flask, request, jsonify
import pickle
import numpy as np

with open('model.pkl', 'rb') as pkl_file: 
    model = pickle.load(pkl_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json)
    features = features.reshape(1, 4)
    prediction = model.predict(features)
    return  jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    
    app.run('localhost', 5000)
