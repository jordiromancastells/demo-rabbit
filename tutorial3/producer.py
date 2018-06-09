#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pika
import sys

credentials = pika.PlainCredentials('jordi', 'jordi')

parameters = pika.ConnectionParameters(host='localhost',
                                       credentials=credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = "info: Hello World!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [x] Sent %r" % message)

connection.close()