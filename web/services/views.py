from django.shortcuts import render
from django.views.generic import TemplateView
import requests

class ListServies(TemplateView):
    template_name = 'templates/services/index.html'

class WeatherView(TemplateView):
    template_name = 'templates/services/weather.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        city = request.POST.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b8a26bb384d449620973d3b744de7977&units=metric"
        response = requests.get(url)
        data = response.json()
        context["json"] = data
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return render(context=self.get_context_data(**kwargs),template_name='templates/services/weather.html',request=request)
    
class MusicView(TemplateView):
    template_name = 'templates/services/music.html'
