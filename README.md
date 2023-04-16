# OpenWeatherMap-API
In this  porject we  use the OpenWeatherAPI  to predict the weather  of a  given  city
In this program, we use the requests module to send an API request to the OpenWeatherMap API and retrieve the current weather data for a given city.

To use the OpenWeatherMap API, you'll need to sign up for an API key on their website. Once you have an API key, replace YOUR_API_KEY with your actual API key in the API_KEY variable.

The get_weather_data() function takes a city argument, which specifies the city for which to retrieve the weather data. The function builds a URL for the API request, sends the request using the requests.get() method, and parses the JSON response using Python's built-in json module.

The function extracts the weather description and temperature data from the response and returns them as a tuple.

Finally, we call the get_weather_data() function with a city name, print the weather description and temperature to the console.
