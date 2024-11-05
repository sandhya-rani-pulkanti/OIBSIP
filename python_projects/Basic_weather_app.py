

import urllib.parse
import urllib.request
import json

def get_coordinates(city_name):
    """Convert city name to latitude and longitude using Nominatim API."""
    try:
        url = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode({
            'q': city_name,
            'format': 'json',
            'limit': 1
        })
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return latitude, longitude
        else:
            print("City not found. Please enter a valid city name.")
    except Exception as e:
        print("Error connecting to the geolocation service:", e)
    return None, None

def get_weather_data(latitude, longitude):
    """Fetch weather data for given coordinates from Open-Meteo API."""
    try:
        url = 'https://api.open-meteo.com/v1/forecast?' + urllib.parse.urlencode({
            'latitude': latitude,
            'longitude': longitude,
            'current_weather': 'true'
        })
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        if 'current_weather' in data:
            return data['current_weather']
        else:
            print("An error occurred while fetching weather data.")
    except Exception as e:
        print("Error connecting to the weather service:", e)
    return None

def display_weather_info(city_name, weather_data):
    """Display the fetched weather information in a readable format."""
    if weather_data:
        temperature = weather_data.get('temperature')
        wind_speed = weather_data.get('windspeed')
        weather_condition = weather_data.get('weathercode')  # Weather condition code
        
        print(f"\nWeather in {city_name.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Speed: {wind_speed} km/h")
        print(f"Weather Condition Code: {weather_condition}")
    else:
        print("No data available to display.")

def main():
    """Main function to run the interactive weather program."""
    print("Welcome to the Basic Weather App!")

    while True:
        city_name = input("Enter a city name (or 'exit' to quit): ").strip()
        
        if city_name.lower() == 'exit':
            print("Exiting the app. Goodbye!")
            break
        
        latitude, longitude = get_coordinates(city_name)
        if latitude is not None and longitude is not None:
            weather_data = get_weather_data(latitude, longitude)
            display_weather_info(city_name, weather_data)

# Run the app
if __name__ == "__main__":
    main()
