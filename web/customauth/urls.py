from django.urls import path
from .views import UserCreationView,LoginView,LogoutView,ProfileView


app_name = "cauth"

urlpatterns = [
    path('register/',UserCreationView.as_view(),name="cauth-register"),
    path('login/',LoginView.as_view(),name="cauth-login"),
    path('logout/',LogoutView.as_view(),name="cauth-logout"),
    path('profile/<int:pk>/',ProfileView.as_view(),name='cauth-profile'),
]