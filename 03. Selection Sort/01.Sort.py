from random import randint

n = 16
a = [ randint(10, 99) for i in range(n)]

print(a)

a.sort() # Ascending order

print(a)

a.sort(reverse = True) # Descending order

print(a)

