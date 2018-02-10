from geopy.geocoders import GoogleV3
from time import sleep

geolocator = GoogleV3("AIzaSyDDwvAnPVqH0cK_-9cYJDxUsanFgjXJduw")
with open("coordinates.txt",'w') as f:
    with open("stationNames.txt",'r') as source:
        for line in source:
            location = geolocator.geocode(line)
            if location:
                lat = location.latitude
                lon = location.longitude
            else:
                lat = None
                lon = None
            coords = "{}, {}".format(lat,lon)
            f.write(coords+'\n')
            sleep(0.3)
