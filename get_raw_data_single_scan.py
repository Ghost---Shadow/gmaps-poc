import requests
import numpy as np
import json

from helpers import *

with open('key.txt','r') as f:
    key = f.read()

lat = 12.9279#latStart + distance / 2
lng = 77.6271#longitudeStart + distance / 2

types = [
    'airport',
    'atm',
    'convenience_store',
    'school',
    'shopping_mall',
    'gym',
    'bank',
    'bar',
    'movie_theater',
    'park',
    'pharmacy',
    'restaurant',
    'police',
    'train_station',
    'place_of_worship'
    ]

# override radius
radius = 2500

##MAX_QUERIES = 3

results = []

for location_type in types:
    print(location_type)
    uri = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=%s&type=%s&key=%s' \
          %(lat,lng,radius,location_type,key)
    #print(uri)
    responseJson = requests.get(uri).json()
    results += responseJson['results']
##    c = 0
##    while 'next_page_token' in responseJson and c < MAX_QUERIES:
##        c += 1
##        newUri = uri + 'next_page_token=%s' % (responseJson['next_page_token'])
##        responseJson = requests.get(uri).json()
##        results += responseJson['results']
    
cachedResult = {}
cachedResult[lat] = {}
cachedResult[lat][lng] = {}
cachedResult[lat][lng]['results'] = results

with open('./data/raw_data.json','w') as f:
    json.dump(cachedResult, f)
    

