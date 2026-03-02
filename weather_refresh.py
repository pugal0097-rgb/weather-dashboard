import requests
import pandas as pd
from datetime import datetime

API_KEY = "8411fe1ba3fb464686c42645260203"
CITY = "Chennai"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

response = requests.get(url)
data = response.json()

record = {
    "City": data["location"]["name"],
    "DateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Temperature": data["current"]["temp_c"],
    "Humidity": data["current"]["humidity"],
    "Wind Speed": data["current"]["wind_kph"],
    "Weather Condition": data["current"]["condition"]["text"]
}

df = pd.DataFrame([record])

file_path = r"C:\DA\Phython.S\weather_project\weather.csv"

try:
    existing = pd.read_csv(file_path)
    df = pd.concat([existing, df], ignore_index=True)
except:
    pass

df.to_csv(file_path, index=False)

print("Weather data updated successfully")