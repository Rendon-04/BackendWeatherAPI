from flask import Flask
import requests
import json 
import os 

lat = 35.6895
lon = 139.6917
API_KEY = os.environ.get("SECRET_KEY")


app = Flask(__name__)
app.api_key = os.environ.get("SECRET_KEY")

response = requests.get("https://api.openweathermap.org/data/2.5/weather",
    params={"lat": lat, "lon": lon, "appid": API_KEY},
    headers={
        "Host": "api.openweathermap.org"
    }
)

print(type(response.json()))
print(response.json())