def validateSubsequence(arr, subseq):

    arrSize = len(arr)
    subseqSize = len(subseq)
    if subseqSize == 0:
        return True
    ptr = 0  # subseq pointer

    for i in range(arrSize):
        if subseq[ptr] == arr[i]:
            ptr += 1
        if ptr == subseqSize:
            return True
    return False


# Driver
arr = [1, 2, 3, 4, 5, 6, 7, 8]
subseq = []
output = validateSubsequence(arr, subseq)
print(output)
