from random import randint

n = int(input('n = '))
a = [randint(10, 20) for i in range(n)]
print(a)

pq = input('p q: ').split()
p, q = int(pq[0]), int(pq[1])

temp = a[p]
a[p] = a[q]
a[q] = temp
# swap(a[p], a[q]) -> C++
print(a)
