import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def index(request):
    appid ='2f3f267a2192c0f2ed053b42293572be'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
        return redirect('/')

    form = CityForm()

    cities = City.objects.all()
    
    all_cities = []
    
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities[::-1], 'form': form}

    return render(request, 'weather/index.html', context)

