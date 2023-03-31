from flask import Flask, jsonify, request, redirect
import requests

app = Flask(__name__)

# API keys for weather APIs
OPENWEATHERMAP_API_KEY = 'd8d10179fb2567f1f926d37ba196dac6'
WEATHERSTACK_API_KEY = '8bf4cf3e35116a2d6a95ed2007450b89'
WINDY_API_KEY = 'y92RGkQxxSNpKjdfgN5IRbBKHNWlXY81' #map forecast API 

# Endpoint to retrieve weather data for a specific location
@app.route('/weather')
def get_weather():
    # Get the location parameter from the request
    location = request.args.get('location')
    
    # Make API requests to the weather APIs
    openweathermap_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}')
    weatherstack_response = requests.get(f'http://api.weatherstack.com/current?access_key={WEATHERSTACK_API_KEY}&query={location}')
    windy_response = requests.get(f'https://api.windy.com/api/forecast/v2.5/access_key={WINDY_API_KEY}')

    # Get the weather data from the responses
    openweathermap_data = openweathermap_response.json()
    weatherstack_data = weatherstack_response.json()
    
    # Combine the weather data from both APIs
    weather_data = {
        'location': location,
        'temperature': {
            'openweathermap': openweathermap_data['main']['temp'],
            'weatherstack': weatherstack_data['current']['temperature']
        },
        'description': {
            'openweathermap': openweathermap_data['weather'][0]['description'],
            'weatherstack': weatherstack_data['current']['weather_descriptions'][0]
        }
    }
    
    # Return the weather data in JSON format
    return jsonify(weather_data)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0",port=3001)