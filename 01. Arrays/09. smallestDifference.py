# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    output = []
    smallestDiff = float('inf')

    arr1Size = len(arr1)
    arr2Size = len(arr2)

    i = 0
    j = 0
    while i < arr1Size and j < arr2Size:
        currDiff = abs(arr1[i] - arr2[j])
        if currDiff < smallestDiff:
            smallestDiff = currDiff
            output = [arr1[i], arr2[j]]

        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            return output

    return output


# Driver
arr1 = [-1, 5, 10, 20, 28, 3]
arr2 = [26, 134, 135, 5, 17]
output = smallestDifference(arr1, arr2)
print(output, end="")
