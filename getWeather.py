#getWeather.py prints the current weather for a given location
import json
import requests
import sys

APPID = 'Your_APPID_Here'

#Get location from the command line
#OpenWeatherMap requires a city name and two-letter country code.
#List of country codes can be found here: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

if len(sys.argv) < 2:
    print('Usage: getWeather.py place_name, 2-letter_country_code')
    sys.exit()
location = ','.join(sys.argv[1:])

print("The location is: " + location)

#Get weather data from openweathermap.org's API in JSON form
url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (location, APPID)
print('Searching: ' + url)
response = requests.get(url)
response.raise_for_status()

#print(response.text)

#Show current weather
#Load JSON data into vairable

weatherData = response.json()
#print(weatherData)

if weatherData["cod"] != "404":
    main_variable = weatherData["main"]

    current_temp = main_variable["temp"]
    current_humidity = main_variable["humidity"]
    weather_variable = weatherData["weather"]
    weather_description = weather_variable[0]["description"]

    print()
    print("The weather in " + location + " is: ")
    print()
    print("Temperature: %.2f" % (current_temp - 273.15) + "°C"
          "\nHumidity: " + str(current_humidity) + "%"
          "\nDescription: " + str(weather_description))

else:
    print("City not found")