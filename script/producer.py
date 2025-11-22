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
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
print(" [x] Sent 'Hello Netology!'")
connection.close()