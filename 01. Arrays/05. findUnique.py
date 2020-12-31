from sys import stdin

def findUnique(arr, N):
    if N == 1:
        return arr[0]
    
    arr = sorted(arr)
    
    for i in range(0, N-1, 2):
        if i == N-1 or arr[i] != arr[i+1]:
            return arr[i]



# Driver
T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split()))
    print(findUnique(arr, N))