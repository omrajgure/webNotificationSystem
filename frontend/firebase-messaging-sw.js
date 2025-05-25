
importScripts('https://www.gstatic.com/firebasejs/9.6.10/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.10/firebase-messaging-compat.js');
importScripts("/firebase_config.js");


firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();



messaging.onBackgroundMessage((payload) => {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  
  const title = payload.notification?.title || 'No Title';
  const body = payload.notification?.body || 'No Body';
  const image = payload.notification?.image;
  const action_url = payload.data?.action_url;

  console.log("Final payload:", title, body, image, action_url);

  const notificationOptions = {
    body,
    icon: image || '/icons/notification-icon.png',
    vibrate: [200, 100, 200],
    data: {
      action_url: action_url || 'http://localhost:3000/index.html'
    }
  };

  self.registration.showNotification(title, notificationOptions);
});


self.addEventListener('notificationclick', function(event) {
  event.notification.close();

  const targetUrl = event.notification.data.action_url;

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then(clientList => {
      for (const client of clientList) {
        if (client.url === targetUrl && 'focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow(targetUrl);
      }
    })
  );
});
