import typer
from typing import Annotated
import json
import requests
from api_key import API_KEY

app = typer.Typer()
user_city = ""

#try:
with open("./data.json", "w+") as file:
    data = json.load(file)
    if data["city"] == None:
        user_city = input("Enter your city: ")
        data["city"] == user_city
        file.dump(data, file, indent = 4)

#
#except (FileNotFoundError, json.decoder.JSONDecodeError):
#    with open("data.json", "w+") as file:
#        user_city = input("Enter your city: ")
#        data = {"city": user_city}
#        json.dump(data, file, indent = 4)
#
@app.command()
def main(user_city: Annotated[str, typer.Argument()] = user_city):
    url_geo_api = "http://api.openweathermap.org/geo/1.0/direct"
    payload_geo_api = {"q": user_city, "appid": API_KEY}
    r_geo_api = requests.get(url_geo_api, params=payload_geo_api)
    data_geo_api = r_geo_api.json()
    user_city_lat = data_geo_api[0]["lat"]
    user_city_lon = data_geo_api[0]["lon"]

    url_current_weather_api = "https://api.openweathermap.org/data/2.5/weather"
    payload_current_weather_api = {"lat" : user_city_lat, "lon" : user_city_lon, "appid" : API_KEY}
    r_current_weather_api = requests.get(url_current_weather_api, params = payload_current_weather_api)
    data_current_weather_api = r_current_weather_api.json()
    print(data_current_weather_api)

if __name__ == "__main__":
    app()
