import json
import numpy as np

from helpers import *

with open('./data/raw_data.json','r') as f:
    raw_data = json.load(f)

newGroup = {}

def processResult(result):
    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']

    lat = truncatedRound(lat)
    lng = truncatedRound(lng)

    if lat not in newGroup:
        newGroup[lat] = {}
    if lng not in newGroup[lat]:
        newGroup[lat][lng] = {}

    newGroup[lat][lng][result['place_id']] = result

for lat in raw_data:
    for long in raw_data[lat]:
        for result in raw_data[lat][long]['results']:
            processResult(result)

for lat in newGroup:
    for lng in newGroup[lat]:
        print(lat, lng, len(newGroup[lat][lng]))

with open('./data/grouped_and_no_duplicates.json','w') as f:
    json.dump(newGroup,f)
