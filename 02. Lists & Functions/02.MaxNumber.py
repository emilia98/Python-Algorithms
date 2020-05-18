a = [10, 45, 67, 89, 34, 91, 15, 18, 34]
n = len(a)

print(a)

max = a[0]

for i in range(1, n):
    if (max < a[i]): max = a[i]

print('Max = ', max)