#!/usr/bin/env python
import pika

# Since we're using default port, we don't have to adjust
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue  to make sure the recipient exist
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World from Python!')
print(" [x] Sent 'Hello World from Python!'")

connection.close()