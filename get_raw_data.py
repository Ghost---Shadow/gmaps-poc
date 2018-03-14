import requests
import numpy as np
import json

with open('key.txt','r') as f:
    key = f.read()

kmToDeg = lambda x: x/111

latStart = 12.95
longitudeStart = 77.7
distance = kmToDeg(5)
steps = 10

latitudes = np.linspace(latStart, latStart + distance, steps)
longitudes = np.linspace(longitudeStart, longitudeStart + distance, steps)

cachedResult = {}

for lat in latitudes:
    cachedResult[lat] = {}
    for long in longitudes:
        print(lat,long)
        uri = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&rankby=distance&key=%s' \
              %(lat,long,key)

        cachedResult[lat][long] = requests.get(uri).json()

with open('./data/raw_data.json','w') as f:
    json.dump(cachedResult, f)
    

