import requests
from django.shortcuts import render

# Create your views here.
def home(request):
    city = "Adama"
    apiKey = "a94b5ab426afd7bceddf051bde36cd48"
    
    currenturl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
    baseUrl = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&units=metric"
    if request.method == "GET":
        city = request.GET.get("city")
        currenturl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
        baseUrl = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&units=metric"
    response = requests.get(baseUrl)
    currentResponse = requests.get(currenturl)
    currentWeather = currentResponse.json()
    weather = response.json()
    current_temp = currentWeather['main']['temp']
    city_name = currentWeather['name']
    current_codnditon = currentWeather['weather'][0]['description']
    current_weather = currentWeather['weather'][0]['icon']

    class Hourly:
        def __init__(self,):
            pass

    context = {
        "current_temp": current_temp,
        "city_name": city_name,
        "current_condition": current_codnditon,
        "current_weather": currentWeather,
    }
    return render(request,'core/home.html',context)