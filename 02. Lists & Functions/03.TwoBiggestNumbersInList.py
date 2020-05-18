from random import randint
n = int(input('n = '))
a = [ randint(10, 99) for i in range(n)]

print(a)

firstMax = a[0]
secondMax = a[1]

for i in range(2, len(a)):
    if (secondMax <= a[i]):
        secondMax = a[i]

    if (firstMax <= secondMax):
        temp = firstMax;
        firstMax = secondMax;
        secondMax = temp;

print('First max = ', firstMax)
print('Second max = ', secondMax)
