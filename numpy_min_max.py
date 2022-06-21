"""
my_array = numpy.array([[2, 5], [3, 7],[1, 3],[4, 0]])

---------min
print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0

-----------max
print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7
"""
import numpy as np
dim = list(map(int,input().split()))
elem = []
for i in range(dim [0]):
    elem.append(list(map(int,input().split())))
elem = np.min(elem, axis = 1)
print(np.max(elem))
