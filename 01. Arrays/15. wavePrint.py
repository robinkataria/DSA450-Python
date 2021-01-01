def wavify(arr, N, M):
    for j in range(M):
        if j % 2 == 0:
            start = 0
            end = N
            step = 1
        else:
            start = N-1
            end = -1
            step = -1

        for i in range(start, end, step):
            print(arr[i][j], end=", ")


# Driver
arr = [[1, 2, 4, 7, 12],
       [2, 5, 19, 31, 32],
       [3, 8, 24, 33, 35],
       [40, 41, 42, 44, 45],
       [99, 100, 103, 106, 128],
       [40, 41, 42, 44, 45]]
wavify(arr, 6, 5)
