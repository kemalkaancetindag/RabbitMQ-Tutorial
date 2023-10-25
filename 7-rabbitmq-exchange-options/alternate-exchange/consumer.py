import pika
from pika.exchange_type import ExchangeType

def alt_queue_on_message_received(ch, method, properties, body):
    print(f"alt exhcange received new message {body}")

def main_queue_on_message_received(ch, method, properties, body):
    print(f"alt exhcange received new message {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(queue="altexchange", exchange_type=ExchangeType.fanout)
channel.exchange_declare(queue="mainexchange", exchange_type=ExchangeType.direct, arguments={
    "alternate-exchange": "altexhcange"
})

channel.queue_declare(queue="altexchangequeue")
channel.queue_bind("altexhangequeue", "altexchange")

channel.queue_declare(queue="mainexchangequeue")
channel.queue_bind("mainexchangequeue", "mainexchange", "test")

channel.basic_consume(queue="altexchangequeue", auto_ack=True, on_message_callback=main_queue_on_message_received)

print("Started consuming")

channel.start_consuming()