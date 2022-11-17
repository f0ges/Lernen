import random
arr = []
for i in range(50):
    a = random.randint(-1000, 1000)
    arr.insert(len(arr), a)
print(arr)
c = len(arr) // 2
for i in range(c):
    b = random.randint(0 ,c)
    arr.pop(b)
print(arr)