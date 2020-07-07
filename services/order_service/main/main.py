from flask import Flask, Response
from json import dumps
import pika
from time import sleep


def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    print()
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


if __name__ == '__main__':
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host='rabbitmq',
                                           virtual_host='/',
                                           port=5672,
                                           credentials=credentials)
    sleep(10)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_consume('hello', on_message)
    print(" [x] Sent 'Hello World!'")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
