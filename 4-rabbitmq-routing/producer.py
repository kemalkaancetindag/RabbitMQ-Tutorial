import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="mytopicexchange", exchange_type=ExchangeType.topic)

user_payment_message = "A european paid for smth"

channel.basic_publish(exchange="mytopicexchange", routing_key="user.europe.payments", body=user_payment_message)

print(f"sent message: {message}")

connection.close()
