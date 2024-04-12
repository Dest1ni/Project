from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class EnterPrivateRoom(LoginRequiredMixin,TemplateView):
    template_name = "chat/index.html"
    login_url = reverse_lazy("cauth:cauth-login")
    success_url = reverse_lazy("chat:chat-enter")


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })