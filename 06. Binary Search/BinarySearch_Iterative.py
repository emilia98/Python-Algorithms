from random import randint

# Returns index of x in array. If not found, returns -1
def binarySearch(arr, x):
    left = 0
    right = len(arr) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2

        # Element could be found at the right subarray,
        # because it's bigger than the current middle
        # element in the subarray
        if arr[mid] < x:
            left = mid + 1

        # Element could be found at the left subarray,
        # because the element is smaller than the
        # current middle element in the subarray
        elif arr[mid] > x:
            right = mid - 1

        # Element is present at the middle itself
        # so we return as a result the middle element index
        else:
            return mid

    return -1

n = 5
arr = [randint(0, 10) for i in range(n)]
x = randint(0, 10)

arr.sort()

print(arr)
print(x)

result = binarySearch(arr, x)

if result != -1:
    print('Element is present at index', str(result))
else:
    print('Element is not present in the array!')
