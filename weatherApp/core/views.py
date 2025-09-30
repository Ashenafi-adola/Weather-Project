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
        def __init__(self,index):
            self.index = index
        def temprature(self):
            return weather['list'][self.index]['main']['temp']
        def icon(self):
            return f"{weather['list'][self.index]['weather'][0]['icon']}.png"
        def time(self):
            return (weather['list'][self.index]['dt_txt'])[-8:-3]

    Hours = [
        Hourly(0),
        Hourly(1),
        Hourly(2),
        Hourly(3),
        Hourly(4),
        Hourly(5),
        Hourly(6),
        Hourly(7),
        Hourly(8),
    ]
    context = {
        "current_temp": current_temp,
        "city_name": city_name,
        "current_condition": current_codnditon,
        "currentWeather": f"{currentWeather['weather'][0]['icon']}.png",
        "Hourly": Hours
    }
    return render(request,'core/home.html',context)