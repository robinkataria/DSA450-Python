# O(n^2) time | O(n) space
def threeNumberSum(arr, targetSum):
    arrSize = len(arr)
    arr.sort()
    out = []

    for i in range(arrSize):

        left = i + 1
        right = arrSize - 1
        for j in range(i+1, arrSize):
            if left >= right:
                break

            currSum = arr[i] + arr[left] + arr[right]
            if currSum == targetSum:
                out.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif currSum > targetSum:
                right -= 1
            else:
                left += 1

    return set(map(tuple, out))


# Driver
# arr = [-1, 0, 1, 2, -1, -4]
arr = [8, 9, 9, 1, 7, 5, 5, 10, 1, 0, 7]
targetSum = 0

output = threeNumberSum(arr, targetSum)
print(*output, sep=", ")
