from geopy.geocoders import GoogleV3
import sqlite3
from time import sleep

class Cache:
    def __init__(self, fn='cache.db'):
       self.conn = conn = sqlite3.connect(fn)
       cur = conn.cursor()
       cur.execute('CREATE TABLE IF NOT EXISTS '
                   'Geo ( '
                   'address STRING PRIMARY KEY, '
                   'latitude DECIMAL(20,17),'
                   'longitude DECIMAL(20,17)'
                   ')')
       conn.commit()

    def address_cached(self, address):
        cur = self.conn.cursor()
        cur.execute('SELECT latitude FROM Geo WHERE address=?', (address,))
        res = cur.fetchone()
        if res is None: return False

    def save_to_cache(self, address, latitude, longitude):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO Geo(address, latitude, longitude) VALUES(?, ?, ?)',
                    (address, latitude, longitude))


geolocator = GoogleV3("AIzaSyDDwvAnPVqH0cK_-9cYJDxUsanFgjXJduw")
with open("stationNames.txt",'r') as source:
    for line in source:
        cache = Cache()
        location = cache.address_cached(line)
        if location:
            continue
        else:
            location = geolocator.geocode(line)
            cache.save_to_cache(line, location.latitude, location.longitude)
        sleep(0.3)

