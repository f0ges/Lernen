import random
arr = []
for i in range(50):
    a = random.randint(-1000, 1000)
    arr.insert(len(arr), a)
print(arr)
