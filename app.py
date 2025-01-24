from flask import Flask
import requests
import json 
import os 

cities = [
    {"name": "San Francisco", "lat": 37.7337, "lon": -122.4312},
    {"name": "San Diego", "lat": 32.7153, "lon": -117.1572},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060}
]

API_KEY = os.environ.get("SECRET_KEY")


app = Flask(__name__)
app.api_key = os.environ.get("SECRET_KEY")
for city in cities:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather",
        params={"lat": city["lat"], "lon": city["lon"], "appid": API_KEY},
        headers={
            "Host": "api.openweathermap.org"
        }
    )

print(type(response.json()))
print(response.json())