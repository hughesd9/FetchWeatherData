#getWeather.py prints the weather for a given location
import json
import requests
import sys

APPID = 'PLACE_API_KEY_HERE'

#TODO
#Get location from the command line
if len(sys.argv) < 2:
    print('Usage: getWeather.py place_name, 2-letter_country_code')
    sys.exit()
location = ''.join(sys.argv[1:])

print(location)


#Get weather data

#Show forecast
