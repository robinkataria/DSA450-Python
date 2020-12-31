def binarySearch(arr, N, ele):
    left = 0
    right = N-1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == ele:
            return mid
        elif ele < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# Driver
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(binarySearch(arr, len(arr), 4))
