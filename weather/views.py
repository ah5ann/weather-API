from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def fahrenheit_to_celsius(fahrenheit_temp):
    return round((fahrenheit_temp - 32) * 5/9)

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5c49ad2de304d462f9b9fee69e294aec'
    
    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']  # Assuming your form has a field 'name'
            
            # Check if the city already exists
            if not City.objects.filter(name=city_name).exists():
                form.save()  # Save if not exists
                return redirect('index')  # Redirect after successful form submission
            else:
                form.add_error(None, 'City already exists.')
    else:
        form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        temperature_fahrenheit = city_weather['main']['temp']
        temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)

        weather = {
            'city': city,
            'temperature': temperature_celsius,
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)
