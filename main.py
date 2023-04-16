import requests

# Replace YOUR_API_KEY with your actual API key from OpenWeatherMap.
API_KEY = "YOUR_API_KEY"

# Define the base URL for the OpenWeatherMap API.
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    """
    Get the current weather data for a given city using the OpenWeatherMap API.
    """
    # Build the URL for the API request.
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"

    # Send the API request and get the response.
    response = requests.get(url)

    # Parse the JSON response and extract the weather data.
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    return weather, temperature

# Example usage: get the weather data for New York City.
city = "New York"
weather, temperature = get_weather_data(city)
print(f"The weather in {city} is currently {weather} with a temperature of {temperature} Kelvin.")
