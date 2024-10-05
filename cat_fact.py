import requests


try:
    response = requests.get('https://catfact.ninja/fact')
    print(response.status_code)
    # indicates if it was successful or not,
    # 200 code means its successful
    # 400s means there's a client error, 500s is a server error
    response.raise_for_status()
    # raise an exception for 400 or 500 code
    print(response.text)
    # text version of response
    print(response.json())
    # json version
    data = response.json()
    fact = data['fact']
    print(f'A random cat fact is {fact}')
except Exception as e:
    print(e)
    print('There was an error making the request.')