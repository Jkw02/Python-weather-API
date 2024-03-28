# send HTTP requests and handle the API response. Make sure 'request' package is installed in python interpreter
import requests
import json

# Base URL and API key from https://openweathermap.org/price by subscribing to Current Weather Data which has data for things like temperature and collect the keys from the 'My API keys' section and make sure base URL has the correct version and the endpoint path.
API_KEY = '[enter api key from website]'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Function to get weather data for a city
def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
# request to the OpenWeatherMap API
    response = requests.get(BASE_URL, params=params)

# additional json module to load JSON data. 200 means that there is a successful response
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to retrieve weather data.")
        return None

# weather conditions dictionary with conditions to descriptions
weather_conditions = {
    'rain': 'It is raining',
    'clouds': 'It is cloudy',
    'clear': 'It is clear',
    'snow': 'It is snowing',
    'thunderstorm': 'There is a thunderstorm',
    'mist': 'There is mist',
    'fog': 'There is fog',
    'smoke': 'There is smoke',
}

#determines whether the weather conditions are suitable for outdoor activities based on weather condition and temperature
def is_suitable_for_activities(weather_data):
    weather_condition = weather_data['weather'][0]['main'].lower()

    if weather_condition in weather_conditions:
        print(weather_conditions[weather_condition])
        return False
    else:
        temperature = weather_data['main']['temp']
        if temperature >= 20:
            return True
        else:
            return False


# List of cities to reduce repetition
cities = ["London", "New York", "Tokyo"]

# take user input and fetch weather data to tell the user if weather is good for outdoors if it reaches threshold temperature of 20 degrees and weather conditions
def main():
    for city in cities:
        weather_data = get_weather_data(city)

        if weather_data:
            if is_suitable_for_activities(weather_data):
                print(f"The weather in {city} is suitable for outdoor activities")
            else:
                print(f"The weather in {city} is not suitable for outdoor activities.")

if __name__ == "__main__":
# Run main when the script is executed
    main()