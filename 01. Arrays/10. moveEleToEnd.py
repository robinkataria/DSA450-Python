# O(n) time | O(1) space
def moveEleToEnd(arr, num):
    i = 0
    j = len(arr) - 1

    while i < j:
        while arr[j] == num:
            j -= 1
        if arr[i] == num:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1


# Driver
arr = [2, 0, 33, 22, 2, 1, 2, 2, 135, 2, 3, 4, 2]
moveEleToEnd(arr, 2)
print(arr)
