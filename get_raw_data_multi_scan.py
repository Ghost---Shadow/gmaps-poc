import requests
import numpy as np
import json

from helpers import *

with open('key.txt','r') as f:
    key = f.read()

latitudes = np.linspace(latStart, latStart + distance, steps)
longitudes = np.linspace(longitudeStart, longitudeStart + distance, steps)

cachedResult = {}

for lat in latitudes:
    cachedResult[lat] = {}
    for long in longitudes:
        print(lat,long)
##        uri = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&rankby=distance&key=%s' \
##              %(lat,long,key)
        uri = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=%s&key=%s' \
              %(lat,long,radius,key)

        cachedResult[lat][long] = requests.get(uri).json()

with open('./data/raw_data.json','w') as f:
    json.dump(cachedResult, f)
    

