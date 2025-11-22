#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('admin', '12345')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='89.169.134.98',
    credentials=credentials
))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()