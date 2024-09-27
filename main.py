import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment variable
API_KEY = os.getenv("WEATHER_API_KEY")

# External API endpoint
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/")
def root():
    return {"message": "Welcome to the Weather API"}

@app.get("/weather/{city}")
def get_weather(city: str):
    # Make a request to the OpenWeatherMap API
    try:
        response = requests.get(WEATHER_API_URL, params={
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # To get the temperature in Celsius
        })
        
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather_info
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error fetching weather data")

