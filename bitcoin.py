import requests

coindesk_url = 'https://claraj.github.io/mock-bitcoin/currentprice.json'

response = requests.get(coindesk_url)
data = response.json()
print(data)
# gets the data from that url
dollars_exchange_rate = data['bpi']['USD']['rate_float']
print(dollars_exchange_rate)
# gets the dollar amount for the exchange rate of bitcoin from the url
bitcoin = float(input('Enter the number of bitcoin: '))

bitcoin_value_in_dollars = bitcoin * dollars_exchange_rate
print(f'{bitcoin} Bitcoin is equal to ${bitcoin_value_in_dollars}')
# tells the client how many total dollars worth of bitcoin they have