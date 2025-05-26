import pika
import json
from backend.app.services.fcm_service import send_push_notification


def callback(ch, method, properties, body):
    try:
        data = json.loads(body)
        token = data['token']
        title = data['title']
        body_text = data['body']
        image_url= data['image_url']
        action_url = data['action_url']
        print(f" [x] Received task for {token}")

        response = send_push_notification(token, title, body_text,image_url,action_url)
        print(f" [✓] Notification sent successfully: {response}")


        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"[!] Error sending notification: {e}")

   

        if "registration token is not a valid" in str(e):

            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        else:

            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='notification_queue', durable=True)


channel.basic_consume(
    queue='notification_queue',
    on_message_callback=callback,
    auto_ack=False  
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


# import firebase_admin
# from firebase_admin import credentials, messaging

# cred = credentials.Certificate("backend/app/config/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# # Dummy token (use a real one from your frontend)
# token = "eIZ_HobQYD7NSfMNGkFfDK:APA91bEhGjTo2pEBV4rg6R3YuQuZg_VV5zcJuI0mIEC8K6b9mHikb01Q-CGYT0XCwP4GC-PC1WxSZf2sYIJZgwH-bEABvjcnkrllQJptCTD6mkXMVuI3HhM"

# message = messaging.Message(
#     notification=messaging.Notification(
#         title="Test Title",
#         body="Test Body",
#     ),
#     token=token,
# )

# response = messaging.send(message)
# print("Successfully sent message:", response)