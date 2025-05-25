import firebase_admin
from firebase_admin import credentials, messaging
import os

if not firebase_admin._apps:
    cred = credentials.Certificate("backend/app/config/serviceAccountKey.json")  
    firebase_admin.initialize_app(cred)

def send_push_notification(token: str, title: str, body: str,image_url: str,action_url: str):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
            image= image_url
            
        ),
        data={
            "action_url": action_url
        },
        token=token
    )

    response = messaging.send(message)
    return response