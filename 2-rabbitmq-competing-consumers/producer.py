import pika
import time
import random

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

message = "Hello this is my first message"

message_id = 1

while(True):
    message = f"Sending message_id: {message_id}"

    channel.basic_publish(exchange="", routing_key="letterbox", body=message)

    print(f"sent message: {message}")
    time.sleep(random.randint(1,3))
    
    message_id += 1
