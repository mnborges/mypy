"""
algoritmo do professor da gabi pra resolução do problema da area

"""
x_ini = 1.0
x_fim = 5.0
N = 10000
delta_x = (x_fim-x_ini)/(N-1)
A = 0.0
for i in range(N):
    if i == 0: continue
    x = x_ini+(i)*delta_x
    A = A + delta_x*x*x

print(A)