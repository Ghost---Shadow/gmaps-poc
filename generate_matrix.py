import numpy as np
import json

from helpers import *

from dot_product_logic import dot_product

with open('./data/grouped_and_no_duplicates.json','r') as f:
    data = json.load(f)

myPreference = [{'name':'atm','weight':2}, {'name':'school','weight':1}]

heatmaps = []
for lat in data:
    for lng in data[lat]:
        names = []
        heat = 0
        for establishment_id in data[lat][lng]:
            establishment = data[lat][lng][establishment_id]
            heat += dot_product(myPreference, establishment)
            names.append(establishment['name'])
        if not len(names) == 0:
            heatmaps.append({'name':names,
                             'lat':lat,
                             'lng':lng,
                             'heat':heat})

jsonData = {'heatmaps':heatmaps}

with open('./data/heatmaps.json','w') as f:
    json.dump(jsonData, f)