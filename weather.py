import requests

api_key = "eb6969714d99e1858cd7b03f0e2c34ec"
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

request = requests.get(url)
json = requests.json()
print(json)