from numpy import array
import requests
import json

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")

import datetime as dt
import time

headers = {
	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com",
	"X-RapidAPI-Key": "" # Register API key at https://rapidapi.com/adsbx/api/adsbexchange-com1/
}
aircraft = "N272BG"
hex_code = "A0FECB"
url = "https://adsbexchange-com1.p.rapidapi.com/v2/hex/" + hex_code + "/"

last_time = 0
last_lat = 0
last_long = 0
while (True):
    response = requests.request("GET", url, headers=headers)

    response = requests.request("GET", url, headers=headers)

    # print(json.dumps(response.json(), indent=2))

    js = response.json()
    lat = js["lat"]
    lon = js["lon"]
    coordinates = str(lat) + " , " + str(lon)
    location = geolocator.reverse(coordinates)
    address = location.raw['address']

    ctime = js["ctime"]

    file_time = dt.datetime.fromtimestamp(ctime)

    if (lat != last_lat or lon != last_lon or last_time != ctime):
        last_lat, last_lon, last_time = lat, lon, ctime
        print("Just landed in: " + str(json.dumps(address)) + " at " +  file_time.strftime("%m %d %Y, %H:%M"))

    time.sleep(60*60)

