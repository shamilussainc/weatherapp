from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=7e4592e56638899b5de85b4456382dc3'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    forms = CityForm
    cities = City.objects.all()

    weather_data = []
    try:
        for city in cities:
            r = requests.get(url.format(city)).json()
            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
    except KeyError:
        pass

    except EXCEPTION as e:
        pass
    context = {
        'weather_data': weather_data,
        'form': forms
    }
    return render(request, 'weather/index.html', context)
