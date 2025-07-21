import llm
import os
import requests
import json

def weather_forecast(city_name: str) -> str:
    """
    This tool predicts the weather for the current and future days based on the name of a city.
    """
    try:
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        geocode_url =  f'https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'
        data = requests.get(url).json()
        lat, lon = data['lat'], data['lon']
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
        data = requests.get(url).json()
        return data
    except Exception as e:
        return f"Error: {str(e)}"

@llm.hookimpl
def register_tools(register):
    register(weather_forecast)
