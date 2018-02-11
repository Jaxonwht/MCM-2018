from geopy.geocoders import GoogleV3
import sqlite3
from time import sleep

class Cache:
    def __init__(self, fn='cache.db'):
       self.conn = conn = sqlite3.connect(fn)
       cur = conn.cursor()
       cur.execute('CREATE TABLE IF NOT EXISTS '
                   'Geo ( '
                   'address TEXT PRIMARY KEY, '
                   'latitude REAL, '
                   'longitude REAL'
                   ')')
       conn.commit()

    def address_cached(self, address):
        cur = self.conn.cursor()
        cur.execute('SELECT latitude FROM Geo WHERE address=?', (address,))
        res = cur.fetchone()
        if res is None: return False
        return True

    def save_to_cache(self, address, latitude, longitude):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO Geo VALUES(?, ?, ?)',
                    (address, latitude, longitude))
        self.conn.commit()

geolocator = GoogleV3("AIzaSyDDwvAnPVqH0cK_-9cYJDxUsanFgjXJduw")
with open("stationNames.txt",'r') as source:
    for line in source:
        cache = Cache()
        location = cache.address_cached(line)
        if location:
            continue
        else:
            location = geolocator.geocode(line)
            if location != None: 
                cache.save_to_cache(line, location.latitude, location.longitude)
            else:
                conn = sqlite3.connect('cache.db') 
                c = conn.cursor() 
                c.execute('INSERT INTO Geo(address) VALUES(?)',(line,))
                conn.commit()
        sleep(0.3)

