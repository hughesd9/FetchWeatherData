#getWeather.py prints the weather for a given location
import json
import requests
import sys

APPID = 'Your_API_key_here'

#TODO
#Get location from the command line
#OpenWeatherMap requires a city name and two-letter country code.
#List of country codes can be found here: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

if len(sys.argv) < 2:
    print('Usage: getWeather.py place_name, 2-letter_country_code')
    sys.exit()
location = ','.join(sys.argv[1:])

print("The location is: " + location)

#Get weather data from openweathermap.org's API in JSON form
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + APPID + "&q=" + location
print('Searching: ' + complete_url)
response = requests.get(complete_url)
response.raise_for_status()

print(response.text)

#Show forecast
