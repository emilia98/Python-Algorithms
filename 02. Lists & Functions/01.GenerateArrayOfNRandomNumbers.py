import random

n = int(input('Въведете едно число: '))
a = [ random.randint(10,20) for i in range(n)]
print(a)