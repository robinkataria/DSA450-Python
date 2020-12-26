def findPair(arr, target):
    d = {}
    for ele in arr:
        adder = target - ele
        if adder in d:
            return [ele, adder]
        else:
            d[ele] = True
    return []


# Driver
arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
output = findPair(arr, target)
print(*output, sep=", ")


# Approach :
# 1. Two for loops >>> O(n^2) time | O(1) space
# 2. Sort, Two pointer >>> O(nlogn) time | O(1) space
# 3. Dictionary >>> O(n) time | O(n) space
