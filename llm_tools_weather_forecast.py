import llm
import os
import requests
import json

def weather_forecast(city_name: str) -> str:
    """
    This tool privides data for predicting the weather for the current and future 5 days based on the name of a city.
    """
    try:
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        geocode_url =  f'https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'
        geocode_data = requests.get(geocode_url).json()
        lat, lon = geocode_data[0]['lat'], geocode_data[0]['lon']
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
        forecast_data = requests.get(forecast_url).json()
        return forecast_data
    except Exception as e:
        return f"Error: {str(e)}"

@llm.hookimpl
def register_tools(register):
    register(weather_forecast)
