import pika
import pickle
import numpy as np
import json

with open('C:\скил\DST-156\IDE_NEW\DS_PROD-3. Сервисная архитектура и оркестрация приложений\microservice_architecture\model\src\myfile.pkl', 'rb') as pkl_file:
    regressor = pickle.load(pkl_file)

try:
    # Создаём подключение по адресу rabbitmq:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
 
    # Объявляем очередь features
    channel.queue_declare(queue='features')
    # Объявляем очередь y_pred
    channel.queue_declare(queue='y_pred')
 
    # Создаём функцию callback для обработки данных из очереди
    def callback(ch, method, properties, body):
        print(f'Получен вектор признаков {body}')
        features = json.loads(body)
        pred = regressor.predict(np.array(features).reshape(1, -1))
        channel.basic_publish(exchange='',
                        routing_key='y_pred',
                        body=json.dumps(pred[0]))
        print(f'Предсказание {pred[0]} отправлено в очередь y_pred')
 
    # Извлекаем сообщение из очереди features
    # on_message_callback показывает, какую функцию вызвать при получении сообщения
    channel.basic_consume(
        queue='features',
        on_message_callback=callback,
        auto_ack=True
    )
    print('...Ожидание сообщений, для выхода нажмите CTRL+C')
 
    # Запускаем режим ожидания прихода сообщений
    channel.start_consuming()
except:
    print('Не удалось подключиться к очереди')
