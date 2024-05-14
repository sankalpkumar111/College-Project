# EduLink/routing.py

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from EduLink.consumers import NotificationConsumer
from django.urls import re_path
from . import consumers
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/notification/', NotificationConsumer),
        ])
    ),
})

# Ensure that urlpatterns is defined correctly with the routing configuration
urlpatterns = [
    re_path(r'ws/staff-notifications/$', consumers.StaffNotificationConsumer.as_asgi()),
]
