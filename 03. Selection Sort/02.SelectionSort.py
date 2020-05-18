from random import randint

# Method for finding the position of element, which is the smallest in the unsorted subarray
def posmin(a, p, q):
    k = p
    for i in range(p + 1, q):
        if (a[k] > a[i]):
            k = i
    return k

n = 16
a = [ randint(10, 99) for i in range(n)]

print(a) # Before sorting

for p in range(n - 1):
    k = posmin(a, p, n)
    a[p], a[k] = a[k], a[p]
    print(a)

print(a) # After sorting