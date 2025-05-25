import pika
import json
import os

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = 5672
RABBITMQ_USER = "guest"
RABBITMQ_PASS = "guest"

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)

def publish_to_queue(message: dict):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                port=RABBITMQ_PORT,
                credentials=credentials
            )
        )
        channel = connection.channel()


        channel.queue_declare(queue="notification_queue", durable=True)

        channel.basic_publish(
            exchange='',
            routing_key='notification_queue',
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)  
        )

        print("Published to queue: {message}")
        channel.close()
        connection.close()
    except Exception as e:
        print("Failed to publish:", str(e))
        raise