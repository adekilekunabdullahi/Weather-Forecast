from datetime import datetime

import geocoder as geocoder
import requests
from django.core.handlers import exception
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from WeatherApp.models import Worldcities


# Create your views here.
def show_temp(request):
    location = geocoder.ip('me').latlng
    temp = get_location(location)
    template = loader.get_template('index.html')
    context = {'temp':temp, 'city': "Your Location:"}
    return HttpResponse(template.render(context, request))


def get_location(location):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.now()
    hour = now.hour
    meteo = requests.get(api_request).json()
    temp = meteo['hourly']['temperature_2m'][hour]
    return temp


def somewhere(request):
    city = request.GET.get('city_name')
    try:
        randoms = Worldcities.objects.get(city=city)
        citi = randoms.city
        location = [randoms.lat, randoms.lng]
        temp = get_location(location)
    except:
        citi = "City Not Found"
        temp = "No data to Show"
    return render(request, "index.html", {'city': citi, 'temp': temp})
