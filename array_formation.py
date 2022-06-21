def canFormArray(self, arr, pieces):
	return
	
print("Let's check if an array of distinct integers can be obtained by concatenating an array of integer arrays - called pieces - with distinct integers as well")
s = input("Please enter integers separeted by ',': ")
arr = s.split(',')
for x in range(len(arr)):
    try: 
        arr[x] = int(arr[x])
    except: 
        print('Error!',arr[x],'is not a integer')
        continue
for x in arr:
    if type(x) != type(0): arr.remove(x)
s = input("Now enter arrays that constitute the array 'pieces', separete arrays with '*' : ")
s = s.split('*')
pieces = []
for x in range(len(s)):
    s[x] = s[x].split(',')
    for i in range(len(s[x])): 
        try:  
               s[x][i] = int(s[x][i])
        except: 
            if s[x][i] != '': 
                print('Error!',s[x][i],'is not a integer')
            continue
        if i <1: pieces.append(s[x])
print('arr = ', arr)
print('pieces = ' , pieces)
"""
for x in range(len(arr)):
    try: 
        arr[x] = int(arr[x])
    except: 
        print('Error!',arr[x],'is not a integer')
        continue
for x in arr:
    #print(type(x))
    if type(x) != type(0): arr.remove(x)
"""