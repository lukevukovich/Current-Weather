import datetime

# Location API
LOCATION_URL = "https://ipgeolocation.abstractapi.com/v1/?api_key="
LOCATION_API_KEY = "b4f32e6bbdf54c8fb882d51a15f04c2e"

# GEO API
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# &units=imperial

# Weather API
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
WEATHER_API_KEY = "8870d0224a58f7c518f0892f6d07e6c3"


# Return float values of weather stats
def get_weather_stats(response):
    t = response['main']['temp']
    maxi = response['main']['temp_max']
    mini = response['main']['temp_min']
    w = response['weather'][0]['main']
    h = response['main']['humidity']
    return t, maxi, mini, w, h


# Return formatted string value to specific decical place
def format_stat(stat, dec):
    f_stat = str(('{:.' + str(dec) + 'f}').format(stat))
    return f_stat


# Print formatted weather results
def print_weather_results(ls, t, ma, mi, w, h):
    # Get timestamp
    d = datetime.datetime.now()
    d = str(d)
    d = d[:-7]
    ls += (" (" + d + "):")

    # Neatly print results
    print(ls)
    print("Temperature: " + t + " F")
    print("Max: " + ma + " F")
    print("Min: " + mi + " F")
    print("Weather: " + w)
    print("Humidity: " + h + "%")

