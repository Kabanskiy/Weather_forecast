from django.shortcuts import render
import requests

def index(request):
    appid = "60925936ffb2aea192fc36034702edba"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    city = 'Petrozavodsk'
    res = requests.get(url.format(city))
    print(res.text)
    return render(request, 'weather/index.html')
