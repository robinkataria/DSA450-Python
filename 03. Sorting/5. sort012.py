# O(n) time | O(1) space
def sort012(arr):
    i = 0
    left = 0
    right = len(arr) - 1

    while i <= right:

        if arr[i] == 1:
            i += 1
        elif arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        else:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1


# Driver
arr = [2, 0, 1]
sort012(arr)
print(arr)
