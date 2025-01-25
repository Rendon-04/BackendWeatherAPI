from flask import Flask
import requests
from dotenv import load_dotenv
import os

load_dotenv()

cities = [
    {"lat": 37.7337, "lon": -122.4312},  # Daly City
    {"lat": 32.7153, "lon": -117.1572},  # San Diego
    {"lat": 40.7128, "lon": -74.0060}    # New York
]

API_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)

for city in cities:
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "lat": city["lat"],
            "lon": city["lon"],
            "appid": API_KEY,
            "units": "imperial"  
        }
    )

    if response.status_code == 200:
        response_data = response.json()

        city_name = response_data["name"]
        temperature = response_data["main"]["temp"]
        weather_description = response_data["weather"][0]["description"]
        humidity = response_data["main"]["humidity"]
        wind_speed = response_data["wind"]["speed"]
        cloudiness = response_data["clouds"]["all"]

        print(f"Weather in {city_name}:")
        print(f"  Temperature: {temperature}°F")
        print(f"  Condition: {weather_description}")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} m/s")
        print(f"  Cloudiness: {cloudiness}%")
    else:
        print(f"Error {response.status_code}: {response.text}\n")
