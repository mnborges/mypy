"""
A = numpy.array([0, 1])
B = numpy.array([3, 4])

--------inner: returns the inner product of two arrays.
info:  This operation associates each pair of vectors in the space 
    with a scalar quantity known as the inner product of the vectors,
print numpy.inner(A, B)     #Output : 4

-------outer: returns the outer product of two arrays.
info: their outer product, denoted u x v, is defined as the m × n matrix A 
    obtained by multiplying each element of u by each element of v

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]

Task

You are given two arrays:  and .
Your task is to compute their inner and outer product.
"""
import numpy as np

A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(np.inner(A,B))
print(np.outer(A,B))