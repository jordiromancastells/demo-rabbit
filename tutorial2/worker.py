#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pika
import time

credentials = pika.PlainCredentials('jordi', 'jordi')

parameters = pika.ConnectionParameters(host='localhost',
                                       credentials=credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

print(' [*] Esperando mensajes... Para salir pulsa  CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Recibiendo %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()