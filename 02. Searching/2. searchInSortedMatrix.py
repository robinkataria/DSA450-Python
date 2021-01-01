def search(arr, N, ele):
    i = 0
    j = N-1

    while(i < N and j >= 0):
        if arr[i][j] == ele:
            return [i, j]
        elif arr[i][j] > ele:
            j -= 1
        else:
            i += 1

    return [-1, -1]


# Driver
arr = [[1, 2, 4, 7, 12],
       [2, 5, 19, 31, 32],
       [3, 8, 24, 33, 35],
       [40, 41, 42, 44, 45],
       [99, 100, 103, 106, 128]]
print(search(arr, len(arr[0]), 993))
