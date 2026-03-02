import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# first Streamlit command
st.set_page_config(page_title="Live Weather Dashboard", layout="wide")

# WeatherAPI key
API_KEY = "8411fe1ba3fb464686c42645260203"

# Title
st.title("🌦️ Real-Time Weather Dashboard")

# City selector
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

# METRICS
col1, col2, col3 = st.columns(3)

col1.metric("Temperature", f"{data['Temperature (°C)']} °C")
col2.metric("Humidity", f"{data['Humidity (%)']} %")
col3.metric("Wind Speed", f"{data['Wind Speed (kph)']} kph")

# TABLE 
st.write("### 📋 Weather Details")
st.dataframe(df, use_container_width=True)

# CHART 
st.write("### 📊 Weather Charts")

fig, ax = plt.subplots(figsize=(6,3))

ax.bar(
    ["Temperature", "Humidity", "Wind Speed"],
    [
        data["Temperature (°C)"],
        data["Humidity (%)"],
        data["Wind Speed (kph)"]
    ]
)

plt.tight_layout()
st.pyplot(fig)

# Footer
st.caption("Data updates automatically each time the page loads.")





