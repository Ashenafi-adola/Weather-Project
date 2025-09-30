import requests
from django.shortcuts import render

# Create your views here.
def home(request):
    city = "Adama"
    apiKey = "a94b5ab426afd7bceddf051bde36cd48"
    
    if request.method == "GET":
        city = request.GET.get("city")
        currenturl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
        baseUrl = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&units=metric"
    response = requests.get(baseUrl)
    currentResponse = requests.get(currenturl)
    currentWeather = currentResponse.json()
    weather = response.json()
    
    context = {

    }
    return render(request,'core/home.html',context)