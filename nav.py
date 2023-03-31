from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)
@app.route('/weather',methods=["POST"])
def get_weather():
    print(request.get_json())
    reqq = request.get_json()
    city = reqq["cityone"]
    print(city)
    api_key = "d8d10179fb2567f1f926d37ba196dac6"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": round(data["main"]["temp"] - 273.15),
            "description": data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"]
        }
        print(weather)
        return weather
    
    elif response.status_code == 404:
        return {"error": "City not found"}
    
    else:
        return {"error": "An error occurred while fetching weather data"}


if __name__ == "__main__":

    # while True:
    #     city = input("Enter a city name (or 'quit' to exit): ")

    #     if city.lower() == "quit":
    #         break

    #     # elif not city.isalpha():
    #     #    print("City name must contain only alphabetic characters or pluses")

    #     else:

    #         weather = get_weather(city)

    #         if "error" in weather:
    #             print(weather["error"])
                
    #         else:
    #             print(f"Weather in {weather['city']}, {weather['country']}:")
    #             print(f"Temperature: {weather['temperature']}°C")
    #             print(f"Description: {weather['description']}")
    
    app.run(host="0.0.0.0",port=3001)