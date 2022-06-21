#print('remove duplicates')
def remove_dup (head):
    d = {}
    li = []
    for x in head:
        d[x] = d.get(x, 0) + 1
    for k, v in d.items():
        if v >= 2:
            continue
        li.append(k)
    return li

list = []
nlist = []
inp = ''
while inp != 'done':
    inp = input("Enter a number or 'done' to finish: ")
    try:
        list.append(int(inp))
    except:
        if inp != 'done' : print('entry must be an integer! try again')
        continue
print(list)
nlist = remove_dup(list)
print(nlist)