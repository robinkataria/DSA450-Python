def zero(arr, N):
    count = 0
    for i in range(N):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1


# Driver
arr = [2, 0, 1, 0, 0, 3, 0, 5, 0]
zero(arr, len(arr))
print(arr)
