from django.urls import path
from .views import ListServies,WeatherView

app_name = "services"

urlpatterns = [
    path('list/',ListServies.as_view(),name='services-list'),
    path('list/weather/',WeatherView.as_view(),name='services-weather'),
]