import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation for weather visuals
lottie_weather = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_kd7fzzde.json")

# Function to fetch weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Streamlit app UI
st.set_page_config(page_title="Weather App", page_icon="🌤", layout="centered")
st.title("🌦 Weather Forecast")
st_lottie(lottie_weather, height=200, key="weather")

api_key = "b91d8296da657b3f28c6663ad9759c04"  # Use Streamlit Secrets for security

city = st.text_input("🏙 Enter a city name:", placeholder="E.g., New York, Tokyo, London")

if st.button("🔍 Get Weather"):
    if city:
        with st.spinner("Fetching weather data..."):
            time.sleep(1.5)  # Simulate loading time
            weather_data = get_weather(city, api_key)
        
        if weather_data.get("cod") != 200:
            st.error(f"❌ Error: {weather_data.get('message', 'City not found!')}")
        else:
            st.success("✅ Weather data retrieved!")
            st.subheader(f"🌍 Weather in {city}")
            st.metric(label="🌡 Temperature", value=f"{weather_data['main']['temp']}°C")
            st.write(f"🌤 Condition: {weather_data['weather'][0]['description'].capitalize()}")
            
            # Display Weather Icon with Animation
            icon_code = weather_data["weather"][0]["icon"]
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            st.image(icon_url, caption=weather_data["weather"][0]["description"].capitalize(), use_column_width=False)
    else:
        st.warning("⚠️ Please enter a city name.")
