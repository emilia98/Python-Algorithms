from random import randint

n = int(input('Брой на числата: '))
a = [randint(11, 99) for i in range(n)]

max = a[0]
min = a[0]

for i in range(1, n):
    if (max < a[i]): max = a[i]

    if (min > a[i]): min = a[i]

print(a)
print("%s%s" % ("Max = ", max))
print("%s%s" % ("Min = ", min))
