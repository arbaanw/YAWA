import typer
import json
import requests
import subprocess
from typing import Annotated
from pathlib import Path
from api_key import API_KEY

URL_GEO_API = "http://api.openweathermap.org/geo/1.0/direct"
URL_CURRENT_WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"

app = typer.Typer()
project_root = Path.cwd()
json_file_path = project_root / "data.json"


def fetch_city_coords(user_city: str):
    payload_geo_api = {"q": user_city, "appid": API_KEY}
    response_geo_api = requests.get(URL_GEO_API, params=payload_geo_api)
    data_geo_api = response_geo_api.json()
    user_city_lat = data_geo_api[0]["lat"]
    user_city_lon = data_geo_api[0]["lon"]
    return (user_city_lat, user_city_lon)

def fetch_weather_data(city, city_coords):
    city_lat, city_lon = city_coords
    payload_current_weather_api = {"lat" : city_lat, "lon" : city_lon, "appid" : API_KEY}
    response_current_weather_api = requests.get(URL_CURRENT_WEATHER_API, params = payload_current_weather_api)
    data_current_weather_api = response_current_weather_api.json()
    return data_current_weather_api

def extract_data(data):
    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]
    description = weather["description"]
    temperature = main["temp"]
    temperature_in_celsius = temperature - 273.15   
    temperature_in_fahrenheit = (temperature - 273.15) * (9/5) + 32
    print(temperature_in_celsius)
    print(temperature_in_fahrenheit)
    feels_like = main["feels_like"]
    feels_like_in_celsius = 273 + feels_like
    pressure = main["pressure"]
    humidity = main["humidity"]
    pressure = main["pressure"]
    

def load_user_defaults():
    try: 
        with open(json_file_path,  "r") as file:
            data = json.load(file)
            user_city_json = data["city"]
            return user_city_json 
    except FileNotFoundError, json.decoder.JSONDecodeError:
        with open(json_file_path,  "w") as file:
            user_city_json = input("Enter your city: ")
            data = {"city": user_city_json}
            json.dump(data, file)
            return user_city_json 

@app.command()
def main(city: Annotated[str, typer.Argument()] = load_user_defaults()):
    city_coords = fetch_city_coords(city)
    data_current_weather_api = fetch_weather_data(city, city_coords)
    print(data_current_weather_api)

@app.command()
def default(city):
    with open(json_file_path,  "w") as file:
        data = {"city": city}
        json.dump(data, file)


if __name__ == "__main__":
    app()
