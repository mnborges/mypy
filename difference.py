"""
ne = int(input())
le = set(map(int, input().split()))
nf = int(input())
lf = set(map(int, input().split()))
#print (len(le.difference(lf)))
print (len(le.symmetric_difference(lf)))
"""
sA = int(input())
A = set(map(int, input().split()))
numOp = int(input())
for i in range(numOp):
    operation = input().split()
    opName = operation[0]
    opSet = set(map(int, input().split()))
    if (opName == 'update'): A.update(opSet)
    elif(opName == 'intersection_update'): A.intersection_update(opSet)
    elif(opName == 'difference_update'): A.difference_update(opSet)
    elif(opName == 'symmetric_difference_update'): A.symmetric_difference_update(opSet)
    else: continue
print(sum(A))