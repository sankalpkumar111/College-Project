# edulink/consumers.py

from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

# Create a consumer class

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        # Called when the WebSocket connection is established
        pass

    def disconnect(self, close_code):
        # Called when the WebSocket connection is closed
        pass

    def receive(self, text_data):
        # Called when a message is received from the WebSocket
        pass

    def send_notification(self, event):
        # Send notification message to the client
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

class StaffNotificationConsumer(WebsocketConsumer):
    def connect(self):
        pass

       

    def disconnect(self, close_code):
        # Leave room group
       pass
   
    def receive(self, text_data):
        # Called when a message is received from the WebSocket
        pass
    # Receive message from room group
    def send_notification(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
