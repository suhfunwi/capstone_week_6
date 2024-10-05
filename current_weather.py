from pprint import pprint
# pprint(pretty print) just makes the output more human-readable
import requests
import os

key = os.environ.get('WEATHER_KEY')
print(key)
# prints out the weather key if it is set in environment variables

url = f'https://api.openweathermap.org/data/2.5/weather'
# uses the key defined above instead of just having it in the code
city = input('Enter the city: ')
country = input('Enter the 2-letter country code: ')
location = f'{city}, {country}'
# to be added to the query
query = {'q': f'{location}', 'units': 'imperial', 'appid': key}
# puts this data in a query for the data variable to access
data = requests.get(url, params = query).json()
# params accesses the query
pprint(data)
temp = data['main']['temp']
# go into the dictionary and retrieve the temp value
print(f'The current temperature is {temp}F')