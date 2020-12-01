
def maxMin(a):
    min = max = 0
    length = len(a)

    for i in range(length):
        if a[i] < a[min]:
            min = i

        if a[i] > a[max]:
            max = i

    return max, min


# Driver
arr = list(map(int, input().split()))
max, min = maxMin(arr)

print("Minimum = " + str(arr[min]))
print("Maximum = " + str(arr[max]))
