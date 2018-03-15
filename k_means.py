import numpy as np
import json

from helpers import *

from sklearn.cluster import KMeans

CLUSTERS = 2

with open('./data/heatmaps.json','r') as f:
    data = json.load(f)

coords = []
for row in data['heatmaps']:
    coords.append([float(row['lat']), float(row['lng'])])

means = KMeans(CLUSTERS).fit(coords)
classes = means.predict(coords)

averageDistances = np.zeros(CLUSTERS)

for i, coord in enumerate(coords):
    cluster = classes[i]
    averageDistances[cluster] += np.linalg.norm(np.array(coord) - means.cluster_centers_[cluster])

unique, counts = np.unique(classes, return_counts=True)
occurances = dict(zip(unique, counts))

for cluster in range(CLUSTERS):
    print(occurances[cluster])
    averageDistances[cluster] /= occurances[cluster]
    print(averageDistances[cluster])

circles = []

for cluster in range(CLUSTERS):
    circles.append({'center':list(means.cluster_centers_[cluster]),
                   'radius':degToKm(averageDistances[cluster]) * KM_TO_M})

outputDict = {'circles':circles}

with open('./data/k_means.json','w') as f:
    json.dump(outputDict,f)
