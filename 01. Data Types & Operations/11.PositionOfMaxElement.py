from random import randint

n = int(input('n = '))
a = [randint(10, 99) for i in range(n)]
print(a)

max = a[0]
p = 0

for i in range(1, n):
    if (max < a[i]):
        max = a[i]
        p = i

print('Max = ', max)
print('Position = ', p)
