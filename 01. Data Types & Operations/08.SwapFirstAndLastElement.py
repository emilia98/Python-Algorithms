from random import randint

n = int(input('n = '))
a = [randint(10, 99) for i in range(n)]
print(a)

a[0], a[n - 1] = a[n - 1], a[0]
print(a)