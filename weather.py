import requests as r

city= input('Which city would you like to know the weather from? \n')

url= 'http://api.weatherapi.com/v1/current.json?key=98ef9630e8bf4c60908103145232908&q='+city+'&aqi=no'
response = r.get(url)


if response.status_code == 200:
    weather_json = response.json()
    location = weather_json.get('location').get('name')
    temp= weather_json.get('current').get('temp_f')
    description=weather_json.get('current').get('condition').get('text')
    print('Todays weather in', city, 'is', description, 'and', temp )
else:
    print('City not found or there was an issue with the API request.')