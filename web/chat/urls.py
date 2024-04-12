from django.urls import path

from .views import *

urlpatterns = [
    path('', EnterPrivateRoom.as_view(), name='chat-enter'),
    path('<str:room_name>/', room, name='chat-room'),
]