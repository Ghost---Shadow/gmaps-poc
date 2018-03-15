import numpy as np
import json

import matplotlib.pyplot as plt

from helpers import *

from dot_product_logic import dot_product

with open('./data/grouped_and_no_duplicates.json','r') as f:
    data = json.load(f)

latitudes = np.linspace(latStart, latStart + distance, resolution)
longitudes = np.linspace(longitudeStart, longitudeStart + distance, resolution)

matrix = np.zeros([resolution, resolution], np.float32)

myPreference = [{'name':'atm','weight':2}, {'name':'school','weight':1}]
##with open('./types.txt','r') as f:
##    allTypes = f.read().split('\n')
##    myPreference = []
##    for aType in allTypes:
##        myPreference.append({'name':aType,'weight':1})


heatmaps = []

for i, lat in enumerate(latitudes):
    for j, lng in enumerate(longitudes):
        lat = str(truncatedRound(lat))
        lng = str(truncatedRound(lng))
        if lat in data:
            if lng in data[lat]:
                names = []
                for establishment_id in data[lat][lng]:
                    establishment = data[lat][lng][establishment_id]
                    matrix[i,j] += dot_product(myPreference, establishment)
                    names.append(establishment['name'])
                heatmaps.append({'name':names,
                                 'lat':lat,
                                 'lng':lng,
                                 'heat':float(matrix[i,j])})

matrix /= np.max(matrix)

jsonData = {'heatmaps':heatmaps}

with open('./data/heatmaps.json','w') as f:
    json.dump(jsonData, f)

np.save('./data/result_matrix.npy', matrix)

plt.imshow(matrix)
plt.show()




        
