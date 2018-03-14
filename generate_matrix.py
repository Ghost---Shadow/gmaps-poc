from helpers import *
import numpy as np
import json

import matplotlib.pyplot as plt

with open('./data/grouped_and_no_duplicates.json','r') as f:
    data = json.load(f)

latitudes = np.linspace(latStart, latStart + distance, resolution)
longitudes = np.linspace(longitudeStart, longitudeStart + distance, resolution)

matrix = np.zeros([resolution, resolution], np.float32)

for i, lat in enumerate(latitudes):
    for j, lng in enumerate(longitudes):
        lat = str(truncatedRound(lat))
        lng = str(truncatedRound(lng))
        if lat in data:
            if lng in data[lat]:
                matrix[i,j] = len(data[lat][lng])

matrix /= np.max(matrix)
plt.imshow(matrix)
plt.show()




        
