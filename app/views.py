from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    city=request.GET.get('city','bengaluru')
    api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7345013238208a620d75879d5ec03e53&units=metric'
    api=requests.get(api_url).json() 
    temperature=api['main']['temp']
    speed=api['wind']['speed']
    humidity=api['main']['humidity']
    cloud=api['weather'][0]['description']
    weather=api['weather'][0]['main']
    icon=api['weather'][0]['icon']
    country=api['sys']['country']
    city_name=api['name']
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    return render(request,"indexpss.html",{'temperature':temperature,'country':country,'city':city_name,'speed':speed,'humidity':humidity,'cloud':cloud,'weather':weather,'icon':icon_url})
