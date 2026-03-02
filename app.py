import streamlit as st
import pandas as pd
import requests

# Your WeatherAPI key
API_KEY = "8411fe1ba3fb464686c42645260203"

# City to fetch weather
city = st.selectbox(
    "Select City",
    ["Chennai", "Mumbai", "Delhi", "Bangalore"]
)

# API request
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
response = requests.get(url).json()

# Extract data
data = {
    "City": response["location"]["name"],
    "DateTime": response["location"]["localtime"],
    "Temperature (°C)": response["current"]["temp_c"],
    "Humidity (%)": response["current"]["humidity"],
    "Wind Speed (kph)": response["current"]["wind_kph"],
    "Condition": response["current"]["condition"]["text"]
}

df = pd.DataFrame([data])
import matplotlib.pyplot as plt

st.write("### 📊 Weather Charts")

fig, ax = plt.subplots(figsize=(4,2))

ax.bar(["Temperature", "Humidity", "Wind Speed"],
       [data["Temperature (°C)"],
        data["Humidity (%)"],
        data["Wind Speed (kph)"]])

st.pyplot(fig)

# Dashboard UI
st.set_page_config(page_title="Live Weather Dashboard", layout="wide")

st.title("🌦️ Real-Time Weather Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Temperature", f"{data['Temperature (°C)']} °C")
col2.metric("Humidity", f"{data['Humidity (%)']} %")
col3.metric("Wind Speed", f"{data['Wind Speed (kph)']} kph")

st.write("### Weather Details")
st.dataframe(df)


st.caption("Data updates automatically each time the page loads.")



