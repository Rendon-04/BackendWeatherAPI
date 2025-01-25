from flask import Flask, jsonify
import requests
from dotenv import load_dotenv
import os


load_dotenv()

cities = [
    {"lat": 37.7337, "lon": -122.4312},  # San Francisco
    {"lat": 32.7153, "lon": -117.1572},  # San Diego
    {"lat": 40.7128, "lon": -74.0060}    # New York
]

API_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def forecasted_weather():
    # Dictionary to store the weather data 
    weather_data = {}

    for city in cities:

        current_weather_response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": city["lat"],
                "lon": city["lon"],
                "appid": API_KEY,
                "units": "imperial"
            }
        )

        forecasted_weather_response = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast",
            params={
                "lat": city["lat"],
                "lon": city["lon"],
                "appid": API_KEY,
                "units": "imperial"
            }
        )

        if current_weather_response.status_code == 200 and forecasted_weather_response.status_code == 200:

            current_weather = current_weather_response.json()
            forecast = forecasted_weather_response.json()

            weather_data[current_weather["name"]] = {
                "current_weather": {
                    "city_name": current_weather["name"],
                    "temperature": current_weather["main"]["temp"],
                    "description": current_weather["weather"][0]["description"],
                    "humidity": current_weather["main"]["humidity"],
                    "wind_speed": current_weather["wind"]["speed"],
                    "cloudiness": current_weather["clouds"]["all"]
                },
                "forecast": [
                    {
                        "time": description["dt_txt"],
                        "temperature": description["main"]["temp"],
                        "description": description["weather"][0]["description"],
                        "humidity": description["main"]["humidity"],
                        "wind_speed": description["wind"]["speed"],
                        "cloudiness": description["clouds"]["all"]
                    }
                    for description in forecast["list"][:5]  
                ]
            }
        else:
            {"error": "Failed to fetch weather data"}


    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
