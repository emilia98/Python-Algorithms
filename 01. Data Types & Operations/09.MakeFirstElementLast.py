from random import randint

n = int(input('n = '))
a = [randint(10, 99) for i in range(n)]
print(a, '<-- преди')

for i in range(0, n - 1):
    a[i], a[i + 1] = a[i + 1], a[i]

print(a, '<-- след')
