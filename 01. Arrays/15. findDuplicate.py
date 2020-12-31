# list of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these, there is a single integer value that is present twice.

def findDuplicate(arr, N):
    arraySum = 0
    for ele in arr:
        arraySum += ele
    return arraySum - ((N-1) * (N-2))//2


# Driver
N = int(input())
arr = list(map(int, input().split()))
print(findDuplicate(arr, N))
