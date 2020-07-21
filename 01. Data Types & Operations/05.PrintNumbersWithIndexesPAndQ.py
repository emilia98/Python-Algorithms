from random import randint

n = int(input('n = '))
a = [randint(10, 20) for i in range(n)]
print(a)

pq = input('p q: ').split()
p, q = int(pq[0]), int(pq[1])

print('a[p] =', a[p])
print('a[q] =', a[q])
