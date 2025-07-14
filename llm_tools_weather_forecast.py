import llm
import os
import requests
import json

def weather_forecast(city_name: str) -> str:
    """
    This function predicts the weather for the current and future days based on the name of a city.
    """
    try:
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + city_name
        data = requests.get(url).json()
        return f'{data["name"]}, {round(int(data["main"]["temp"])-273.15, 1)}°C, {data["weather"][0]["description"]}'
    except Exception as e:
        return f"Error: {str(e)}"

@llm.hookimpl
def register_tools(register):
    register(weather_forecast)
