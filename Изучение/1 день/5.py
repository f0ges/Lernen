import random
a = []
num = 4
u = 1
for i in range(num):
    w = []
    for j in range(num):
        rnd = random.randint(0, 9)
        w.append(rnd)
    a.append(w)


for i in(range(num)):
    for j in range(num):
        print(a[i][j], end="")
    print()
