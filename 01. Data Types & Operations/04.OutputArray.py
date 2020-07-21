s = input('Въведи числа: ')
a = s.split()
n = len(a)

for i in range(n):
    a[i] = int(a[i])

print(a)
