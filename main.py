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
country = input("Enter Country: ")

state = ""
if country == 'US':
    state = input("Enter State: ")

city = input("Enter City: ")

# Request to get location
geo_url = "http://api.openweathermap.org/geo/1.0/direct?q="
geo_url += city + "," + state + "," + country + "&limit=5&appid=" + API_KEY
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

    high = weather_response['main']['temp_max']
    high = str('{:.2f}'.format(high))

    low = weather_response['main']['temp_min']
    low = str('{:.2f}'.format(low))

    weather = weather_response['weather'][0]['main']

    if state != "":
        print("\n" + city + ", " + state + " Results:")
    else:
        print("\n" + city + ", " + country + " Results:")
    print("Temperature: " + temp + " F")
    print("High: " + high + " F")
    print("Low: " + low + " F")
    print("Weather: " + weather)

else:
    # If geo request has no body
    print("\nLocation not found")
