# http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&appid=467f53457e603c993afd3aaf7347bbfb

import os
import requests
from pprint import pprint
from _datetime import datetime

key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()

pprint(data)

list_of_forecasts = data['list']
for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    # gets the temp value from the main list
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    # gets the datetime value
    print(f'At {forecast_date} the temperature will be {temp}F.')
    # will print out each individual interval
    # of forecast temperature and date recorded each on separate lines