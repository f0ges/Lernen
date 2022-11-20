from random import randint
m = []
n = int(input("Размер матрицы? :"))
for i in range(n):
    w=[]
    for j in range(n):
        w.append(randint(0,9))
    m.append(w)
for i in range(n):
    r = m[i]
    sum = 0
    for j in range(n):
        print(m[i][j], end=' ')
    print()