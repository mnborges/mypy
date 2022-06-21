"""
my_array = numpy.array([ [1, 2], [3, 4] ])

---------mean: arithmetic mean along the specified axis.
print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5

---------var: arithmetic variance along the specified axis.
print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25

------std: arithmetic standard deviation along the specified axis.
print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
"""
import numpy as np
dim = list(map(int,input().split()))
elem = []
for i in range(dim [0]):
    elem.append(list(map(int,input().split())))
print(np.mean(elem, axis = 1))
print(np.var(elem, axis = 0))
if (np.std(elem) != 0): print("%.11f" % np.std(elem))
else: print(np.std(elem))