import requests
import json
import random
import math
import webbrowser
import datetime

lat = round(random.uniform(-90, 90), 3)
long = round(random.uniform(-180, 180), 3)

api_key = "4227acbc68f3bc395c6eef94f436ba26"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, long, api_key)
response = requests.get(url)
data = json.loads(response.text)

feelz = data['current']['feels_like']
temp = data['current']['temp']
humidity = data['current']['humidity']
sunrise = datetime.datetime.fromtimestamp(data['current']['sunrise'])
sunset = datetime.datetime.fromtimestamp(data['current']['sunset'])

wd = data['current']['weather'][0]['description']
weather = wd.title()

maps_link = f'https://www.google.com/maps/place/{lat}, {long}'


print(f'Your Random Location is: \n\n\tLatitude: {lat} \n\tLongitude: {long}')
print(f'\n\tIt is currently {temp} degrees fahrenheit.')
print(f'\n\tThe current humidity level is {humidity}%')
print(f'\n\tThe weather outside is currently {weather}')
print(f'\n\tThe Sun rose at: \n\t{sunrise}\n\n\tThe Sun will be setting at: \n\t{sunset}')
print('\n\tLaunching Google Maps...')

with open('weather_dump.txt', 'a') as f:
    f.write(f'\n*******************************************\n\nLocation:\n\tLatitude:{lat}, Longitude:{long}\n\nTemperature:\n\t{temp} degrees F\n\nHumidity: \n\t{humidity}%\n\nSunrise time:\n\t{sunrise}\n\nSunset time:\n\t{sunset}\n\nGoogle Maps Link:\n\t{maps_link}\n\n')

launch = webbrowser.open(f'https://www.google.com/maps/place/{lat},{long}')
