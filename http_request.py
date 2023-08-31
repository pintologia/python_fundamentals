# python -m venv venv    

import requests as r

response = r.get('http://api.open-notify.org/astros.json')

json = response.json()

print(json)