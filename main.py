import requests


# GEO URL
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# &units=imperial

# CUR WEATHER URL
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

API_KEY = "8870d0224a58f7c518f0892f6d07e6c3"


def get_lat_long(response):
    return response[0]['lat'], response[0]['lon']


# Get state and city input from user
state = input("Enter State: ")
city = input("Enter City: ")

# Request to get location
geo_url = "http://api.openweathermap.org/geo/1.0/direct?q="
geo_url += city + "," + state + ",US&limit=5&appid=" + API_KEY
geo_response = requests.get(geo_url).json()

# If location was found
if len(geo_response) > 0:

    # Get coordinates of location found
    lat, long = get_lat_long(geo_response)
    lat = str(lat)
    long = str(long)

    # Request for weather of coordinates
    weather_url = "https://api.openweathermap.org/data/2.5/weather?lat="
    weather_url += lat + "&lon=" + long + "&appid=" + API_KEY + "&units=imperial"
    weather_response = requests.get(weather_url).json()

    # Get temp value
    temp = weather_response['main']['temp']
    temp = str('{:.2f}'.format(temp))

    feels_like = weather_response['main']['feels_like']
    feels_like = str('{:.2f}'.format(feels_like))

    weather = weather_response['weather'][0]['main']

    print("\n" + city + ", " + state + " Results:")
    print("Temperature: " + temp + " F")
    print("Feels Like: " + feels_like + " F")
    print("Weather: " + weather)

else:
    # If geo request has no body
    print("Location not found")
