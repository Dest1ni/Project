from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,LogoutView as BaseLogoutView
from .models import UserModel
from .forms import UserCreationForm

class UserCreationView(CreateView):
    model = UserModel
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy("posts:show-posts")

class LoginView(BaseLoginView):
    next_page = reverse_lazy("main-page")
    template_name = 'registration/login.html'

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy("main-page")