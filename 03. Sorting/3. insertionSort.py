# O(n^2) time | O(1) space
def insertionSort(arr, N):
    for i in range(1, N):
        curr = i
        j = i-1
        while j >= 0 and arr[curr] < arr[j]:
            arr[curr], arr[j] = arr[j], arr[curr]
            curr -= 1
            j -= 1


# Driver
arr = [2, 3, 1, 0, 5, -1, 6, 10, 8, 7]
insertionSort(arr, len(arr))
print(arr)
