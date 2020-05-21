from random import randint

n = 10
a = [randint(10, 150) for i in range(n)]

print(a)

for i in range(n):
    x = a[i]
    pos = i - 1

    while pos >= 0 and a[pos] < x:
        a[pos + 1] = a[pos]
        pos -= 1

    a[pos + 1] = x

print(a)