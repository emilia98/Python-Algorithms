import random

def max(a, p, q):
    x = a[p]
    for i in range(p + 1, q):
        if (x < a[i]): x = a[i]
    return x

n = 16
a = [ random.randint(10, 99) for i in range(n)]

print(a)

print('Max = ', max(a, 0, n))