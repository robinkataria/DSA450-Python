# O(n^2) time | O(1) space
def selectionSort(arr, N):
    for i in range(N):
        currMin = i
        for j in range(i+1, N):
            if arr[j] < arr[currMin]:
                currMin = j
        arr[i], arr[currMin] = arr[currMin], arr[i]


# Driver
arr = [2, 3, 1, 0, 5, -1, 6, 10, 8, 7]
selectionSort(arr, len(arr))
print(arr)
