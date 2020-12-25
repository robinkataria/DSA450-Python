def spiral(arr, N, M):
    sR = 0
    eR = N-1

    sC = 0
    eC = M-1

    totalEle = N*M
    x = 0
    output = []

    while x != totalEle:
        for i in range(sC, eC+1):
            output.append(arr[sR][i])
            x += 1
        sR += 1

        for i in range(sR, eR+1):
            output.append(arr[i][eC])
            x += 1
        eC -= 1

        for i in range(eC, sC-1, -1):
            output.append(arr[eR][i])
            x += 1
        eR -= 1

        for i in range(eR, sR-1, -1):
            output.append(arr[i][sC])
            x += 1
        sC += 1

    return output


# Driver
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16],
       [17, 18, 19, 20]]

print(spiral(arr, 5, 4))
