#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pika
import sys

LIMIT = 100000

credentials = pika.PlainCredentials('jordi', 'jordi')

parameters = pika.ConnectionParameters(host='localhost',
                                       credentials=credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def message(x):
    return 'Hello World! ('+str(x)+')'

properties = pika.BasicProperties(delivery_mode= 2) # make message persistent)

for x in range(LIMIT):
    print(' Enviendo: '+message(x))
    channel.basic_publish(exchange='',
                        routing_key='task_queue',
                        body=message(x),
                        properties=properties)
print(" [x] Sent %r" % message)
connection.close()