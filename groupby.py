print("groupby")
from itertools import groupby

data = [('A', 2), ('B', 7), ('F', 8)]
data = sorted(data)
keys = ('B', 'F')
for k, g in groupby(sorted(data),keys): print(k, g)