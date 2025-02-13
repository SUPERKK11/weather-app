import streamlit as st
import requests

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

# Streamlit app
st.title("Weather Chatbot")

api_key = "b91d8296da657b3f28c6663ad9759c04" # Use secrets for API key security

city = st.text_input("Enter a city name:")

if st.button("Get Weather"):
    if city:
        weather_data = get_weather(city, api_key)
        if weather_data.get("cod") != 200:
            st.error(f"Error: {weather_data.get('message', 'City not found!')}")
        else:
            st.subheader(f"Weather in {city}")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")

            # Display Weather Icon
            icon_code = weather_data["weather"][0]["icon"]
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            st.image(icon_url, caption=weather_data["weather"][0]["description"].capitalize())
    else:
        st.error("Please enter a city name.")
