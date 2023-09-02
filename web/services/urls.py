from django.urls import path
from .views import ListServies,WeatherView,MusicView

app_name = "services"

urlpatterns = [
    path('list/',ListServies.as_view(),name='services-list'),
    path('list/weather/',WeatherView.as_view(),name='services-weather'),
    path('list/music/',MusicView.as_view(),name='services-music')
]