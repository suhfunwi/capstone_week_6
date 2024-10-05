import os
from datetime import datetime

import requests
from pprint import pprint

from forecast import timestamp

# Minneapolis
lat = 44.97
lon = -93.26
units = 'imperial'  # change to 'imperial' for quantities in Fahrenheit, miles per hour etc.

api_key = os.environ['WEATHER_KEY']  # Set this environment variable on your computer


url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'

response = requests.get(url)
if response.status_code != 200:
    print(f'Something went wrong. Error: {response.status_code} - {response.text}')
#     error handling, will provide a link if the api crashes
else:
    weather_forecast = response.json()
    pprint(weather_forecast)

    for forecast in weather_forecast['list']:
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        # index to get the first item
        wind_speed = forecast['wind'] ['speed']
        timestamp = forecast['dt']
        forecast_date = datetime.fromtimestamp(timestamp)

        output = {
            'date': forecast_date.strftime('%Y-%m-%d %H:%M:%S'),
            # had to look up how to format it so it's more readable
            'temperature': temp,
            'wind speed': wind_speed,
            'description': description

        }
        pprint(output)

