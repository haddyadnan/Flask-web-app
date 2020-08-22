import requests

url = 'http://localhost:5000/results'
x = requests.post(url,json={})

print(x.json())
