latStart = 12.95
longitudeStart = 77.7
steps = 10
resolution = 100

kmToDeg = lambda x: x/111
degToKm = lambda x: x * 111
truncatedRound = lambda x: round(float(x) * resolution) / resolution

WIDTH = 5
PACKING_FACTOR = 2
KM_TO_M = 1000

radius = round((WIDTH * KM_TO_M * PACKING_FACTOR)/ steps ) 
distance = kmToDeg(WIDTH)


