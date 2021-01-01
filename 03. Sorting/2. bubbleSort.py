# O(n^2) time | O(1) space
def bubbleSort(arr, N):
    for i in range(N-1):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver
arr = [2, 3, 1, 0, 5, -1, 6, 10, 8, 7]
bubbleSort(arr, len(arr))
print(arr)
