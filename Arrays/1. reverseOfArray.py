
def reverse(a):
    i = 0
    j = len(a) - 1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


# Driver
arr = list(map(int, input().split()))
reverse(arr)
print(*arr)

# print(a[::-1])
