from itertools import combinations_with_replacement
inp = input()
S = sorted(inp[:-2])
k = int(inp[-1])
idx = 1
while idx<=k:
    comb = list(combinations_with_replacement(S,idx))
    for tup in comb:
        str = ""
        for elem in tup:
            str += elem
        print (str)
    idx+=1