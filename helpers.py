latStart = 12.95
longitudeStart = 77.7
steps = 10
resolution = 1000

kmToDeg = lambda x: x/111
truncatedRound = lambda x: round(float(x) * resolution) / resolution

distance = kmToDeg(5)


