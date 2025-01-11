from flask import Flask, request, jsonify
import pickle
import numpy as np

# загружаем модель из файла
with open('C:\скил\DST-156\IDE_NEW\DS_PROD-2. Воспроизводимость и контейнеризация приложений\web\app\models\model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg

@app.route('/predict', methods=['POST'])
def predict():
    #ваш код здесь
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)