# stąd nadajemy POSTy do aplikacji
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "apirest/tim/19")
print(response.json())

