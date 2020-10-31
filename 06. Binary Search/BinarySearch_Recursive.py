from random import randint

# Returns index of x in array. If not found, returns -1
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = (l + r) // 2

        # Element is present at the middle itself
        if arr[mid] == x:
            return mid
        # Element could be found at the left subarray,
        # because the element is smaller than the
        # current middle element in the subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        # Element could be found at the right subarray,
        # because it's bigger than the current middle
        # element in the subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


n = 5
arr = [randint(0, 10) for i in range(n)]
x = randint(0, 10)

arr.sort()

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print('Element found at position %d' % result)
else:
    print('Element not found')