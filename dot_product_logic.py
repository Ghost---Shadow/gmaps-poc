import numpy as np

with open('./types.txt','r') as f:
    types = f.read().split('\n')

inverseTypes = {}
for i, type_element in enumerate(types):
    inverseTypes[type_element] = i

def dot_product(preference, establishment):
    p = np.zeros(len(types))
    for type_element in preference:
        try:
            p[inverseTypes[type_element['name']]] = type_element['weight']
        except:
            #print('Key does not exist',type_element)
            pass
    
    e = np.zeros(len(types))
    if 'rating' in establishment:
        score = establishment['rating']
    else:
        score = 2.5
              
    for type_element in establishment['types']:
        try:
            e[inverseTypes[type_element]] = score
        except:
            #print('Key does not exist',type_element)
            pass

    return np.dot(p,e)

#establishment = {}
#establishment['types'] = ['school','campground','casino']
#establishment['rating'] = 5
#preference = [{'name':'casino','weight':2}, {'name':'campground','weight':1}]
#print(dot_product(preference,establishment))
