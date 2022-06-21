"""
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

--------dot: The dot tool returns the dot product of two arrays.
print numpy.dot(A, B)       #Output : 11
---------cross: The cross tool returns the cross product of two arrays.
print numpy.cross(A, B)     #Output : -2
"""
import numpy as np
N = int(input())
A, B = [], []
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
print(np.dot(np.matrix(A),np.matrix(B)))
""" THIS PART I DID WHEN I DIDNT KNOW ABOUT THE EXISTANCE OF THE matrix() METHOD
IT WORKS BUT IT HAS JUST TOO MANY INFORMATION
ALL OF THIS CAN BE REPLACED WITH ONLY 1 LINE OF CODE
sol = {}
index =0
for elem in B:
    for i in elem:
        sol.setdefault(index,list())
        sol[index].append(i)
        index+=1
    index =0
line = ''
print('[', end= '')
for i in range(N):
    if i ==0: print('[', end='')
    else: print(' [', end='')
    for j in range(N):
        line = line+str(np.dot(A[i], sol[j]))
        if j != N-1 : line = line+ ' '
    print(line.rjust(5), end= '')
    line = ''
    if i !=N-1: print(']')
    else: print(']',end='')
print(']')

"""