import requests
data = requests.get('https://random-data-api.com/api/restaurant/random_restaurant')
print(str(data.text))