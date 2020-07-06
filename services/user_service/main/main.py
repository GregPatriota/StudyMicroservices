from flask import Flask, Response
from json import dumps
import pika

app = Flask(__name__)
# rpc = RpcProxy(dict(
#         AMQP_URI='amqp://guest:guest@localhost:5672//'
#     ))


@app.route('/')
def hello_world():
    # parameters = pika.URLParameters('amqp://guest:guest@localhost:5672//')
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host='localhost',
                                           virtual_host='rabbitmq_1',
                                           port=5672,
                                           credentials=credentials)
    connection = pika.BlockingConnection(pika.ConnectionParameters(parameters))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
    return Response(response=dumps({'msg': 'Hello World'}),
                    content_type='Application/json',
                    status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)