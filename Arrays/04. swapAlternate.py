
def swapAlternate(a, n) :
	i = 0
	while i < (n-1) :
		a[i], a[i+1] = a[i+1], a[i]
		i += 2


# Driver
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    swapAlternate(arr, N)
    print(*arr, sep=" ")