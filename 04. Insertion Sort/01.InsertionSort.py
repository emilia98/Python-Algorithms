from random import randint

n = 10
a = [randint(10, 150) for i in range(n)]

print(a)

for i in range(n):
    x = a[i]  # Element on current position 'i'
    pos = i - 1  # The position from which we should start moving elements

    # Move elements from a[0, ..., i - 1] with one position ahead of their current position
    # This happens until we reach the beginning of the array or an element which is smaller
    # than the element we want to move
    while (pos >= 0 and a[pos] > x):
        a[pos + 1] = a[pos]
        pos -= 1

    a[pos + 1] = x

print(a)