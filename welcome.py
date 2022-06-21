N, M = input().split()
N = int(N)
M = int(M)
print(N, M)
c = '.|.'
fill = int((M-3)/2)
for i in range(int((N-1)/2)):
    print((c*i).rjust(fill,'-')+c+(c*i).ljust(fill,'-'))
print('WELCOME'.center(M,'-'))
for i in reversed(range(int((N-1)/2))):
    print((c*i).rjust(fill,'-')+c+(c*i).ljust(fill,'-'))