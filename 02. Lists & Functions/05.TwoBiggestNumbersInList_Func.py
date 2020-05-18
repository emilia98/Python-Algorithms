from random import randint

# Find the position of max element
def posmax(a, p, q):
    k = p
    for i in range(p + 1, q):
        if(a[k] < a[i]): k = i;

    return k

n = 16
a = [ randint(10, 99) for i in range(n)]

# Print 'a' after generating the list
print(a)

# Find the position of max element
k = posmax(a, 0, n)
x = a[k]

# Swap the values of max element and the last element
a[k], a[n - 1] = a[n - 1], a[k]

# Find the second max element
m = posmax(a, 0, n - 1)
y = a[m]

print(x, y)

# The max two numbers to be at the end of the list
a[m], a[n - 2] = a[n - 2], a[m]

print(a)