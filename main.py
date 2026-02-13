import typer
import json
import requests
from typing import Annotated
from pathlib import Path
from api_key import API_KEY

URL_GEO_API = "http://api.openweathermap.org/geo/1.0/direct"
URL_CURRENT_WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"
DEFAULT_UNITS = "Celcius"
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

def load_user_city():
    try: 
        with open(json_file_path,  "r") as file:
            data = json.load(file)
            saved_city = data["city"]
            return saved_city 
    except FileNotFoundError, json.decoder.JSONDecodeError:
        with open(json_file_path,  "w") as file:
            saved_city = input("Enter your city: ")
            data = {"city": saved_city}
            json.dump(data, file)
            return saved_city 

def main(city):
    city_coords = fetch_city_coords(city)
    data_current_weather_api = fetch_weather_data(city, city_coords)
    temp = (data_current_weather_api["main"]["temp"])-273.15
    feels_like = (data_current_weather_api["main"]["feels_like"])-273.15
    print(f"{city.upper()}: {round(temp)}°C (feels like {round(feels_like)}°C)")

def change_default_city(default_city):
    with open(json_file_path,  "r") as file:
        data = json.load(file)
        data["city"] = default_city
    with open(json_file_path, "w") as file:
        print(data)
        json.dump(data, file)



@app.command()
def weather(city: Annotated[str, typer.Argument()] = load_user_city(), change_city: Annotated[str, typer.Option()] = None):

    if change_city != None:
        change_default_city(change_city)
        return

    main(city)
    



if __name__ == "__main__":
    app()
