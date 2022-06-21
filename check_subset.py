"""
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.
RESOLUTION: 
T = int(input())
for i in range(T):
    nA = int(input())
    A = set(map(int,input().split()))
    nB = int(input())
    B = set(map(int,input().split()))
    print(A - B == set())
"""
print('check_subset')
"""
You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
"""
A = set(map(int,input().split()))
n = int(input())
res = True
for i in range(n):
    sub = set(map(int,input().split()))
    res = res and (sub - A == set()) and (A - sub != set())
print(res)