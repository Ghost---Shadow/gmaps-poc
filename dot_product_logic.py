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
            p[inverseTypes[type_element]] = 1
        except:
            #print('Key does not exist',type_element)
            pass
    
    e = np.zeros(len(types))
    for type_element in establishment['types']:
        try:
            e[inverseTypes[type_element]] = 1
        except:
            #print('Key does not exist',type_element)
            pass

    return np.dot(p,e)

##establishment = {}
##establishment['types'] = ['school','campground','casino']
##preference = ['casino', 'campground']
##print(dot_product(preference,establishment))
