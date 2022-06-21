"""
You are given a 2-D array with dimensions N x X.
Your task is to perform the sum tool over axis 0 and then find the prod of that result.
-----------sum
my_array = numpy.array([ [1, 2], [3, 4] ])
print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10

-----------prod
my_array = numpy.array([ [1, 2], [3, 4] ])
print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
"""
import numpy as np
dim = list(map(int,input().split()))
elem = []
for i in range(dim [0]):
    elem.append(list(map(int,input().split())))
elem = np.sum(elem, axis = 0)
print(np.prod(elem))
