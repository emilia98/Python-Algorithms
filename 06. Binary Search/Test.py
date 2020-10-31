from random import randint

# Returns index of x in array. If not found, returns -1
def binarySearch(arr, x):
    print('  l    r   mid   arr[mid]   x =', x)
    print('======================================')
    # left border of interval
    l = 0
    # right border of interval
    r = len(arr) - 1

    # while left border of interval is before the right border of interval
    while l <= r:
        # find the index of middle element in the subarray
        mid = (l + r) // 2
        print(f'{l:2}   {r:2}   {mid:2}     {arr[mid]:2}    ', end='')

        # if x is smaller than the middle element in the array
        # we move the right border with one position
        # on the left of the middle element
        if x < arr[mid]:
            print(x, '<', arr[mid])
            r = mid - 1
        # if x is bigger than the middle element in the array
        # we move the left border with one position
        # on the right of the middle element
        elif x > arr[mid]:
            print(x, '>', arr[mid])
            l = mid + 1
        # if the element x is equal of the middle element
        # in the array, we return the index
        # of the middle element
        else:
            print(x, '=', arr[mid])
            return mid

    print(f'{l:2}   {r:2}')
    # if the searched element x had not found in the given array
    # the returned result is -1
    return -1



arr = [ 10, 15, 20, 30, 35, 40, 50, 56, 58, 60, 62, 63, 80, 88, 90, 95]
n = len(arr)
arr.sort()
print(arr)

x = int(input('x = '))
print()

for i in range(n):
    print(f'{i:2}   ', end='')

print()

for i in range(n):
    print(f'{arr[i]:2}  ', end='')

print()
print()

# calling the function, which finds if the
# searched element is found
mid = binarySearch(arr, x)

if mid >= 0:
    print('Found at position', mid)
else:
    print('Not found')