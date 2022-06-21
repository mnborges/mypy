"""
The NumPy module also comes with a number of built-in routines for linear algebra calculations.
These can be found in the sub-module linalg.
--------linalg.det: computes the determinant of an array.
print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

------linalg.eig: computes the eigenvalues and right eigenvectors of a square array.
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]

-----linalg.inv: computes the (multiplicative) inverse of a matrix.

print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]

other routines: https://numpy.org/doc/stable/reference/routines.linalg.html

Task

You are given a square matrix A with dimensions NxN. Your task is to find the determinant. 
Note: Round the answer to 2 places after the decimal.
"""
import numpy as np
N = int(input())
A = []
for i in range(N):
    A.append(list(map(float,input().split())))
print(round(np.linalg.det(np.matrix(A)),2))