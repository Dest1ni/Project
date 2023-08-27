from django.urls import path
from .views import UserCreationView,LoginView,LogoutView

app_name = "cauth"

urlpatterns = [
    path('register/',UserCreationView.as_view(),name="cauth-register"),
    path('login/',LoginView.as_view(),name="cauth-login"),
    path('logout/',LogoutView.as_view(),name="cauth-logout"),
]