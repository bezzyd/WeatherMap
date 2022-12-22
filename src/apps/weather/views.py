import requests
from django.shortcuts import render

def index(request):
    appid ='32f0bec51d94bd23af99ccede389a86b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

    city = 'London'
    response = requests.get(url.format(city))
    print(response.text)

    return render(request, 'weather/index.html')
