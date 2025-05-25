# Web Notification System with FCM, RabbitMQ and Python

A real-time web notification system using Firebase Cloud Messaging (FCM), RabbitMQ, and a Python backend. Frontend is built with HTML, CSS, and JavaScript.
[Click here to see the demo](https://your-demo-link.netlify.app)

- Frontend: HTML, CSS, JavaScript
- Backend: Python (FastAPI)
- Messaging: Firebase Cloud Messaging (FCM)
- Queue: RabbitMQ
- Containerization: Docker, Docker Compose


## 🔧 Local Development

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/fcm-rabbitmq-project.git
   cd fcm-rabbitmq-project

2. Start using Docker Compose:
    docker-compose up --build

3. Open frontend:
    Navigate to http://localhost:3000 (or whichever port you’re using)

4. Firebase Setup:
    Add your Firebase config in frontend/index.html
	Place your firebase-messaging-sw.js in the root of frontend/

5. 🧪 **API Documentation**

    ### POST /devices/register
        Registers a new device token to receive push notifications.

    ### POST /notifications/publish
        Sends a push notification to all registered tokens.