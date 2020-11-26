
def kadane(A) :
    size = len(A)
    curr_max = global_max = A[0]
    
    for i in range(1, size):
        curr_max = max(A[i], A[i] + curr_max)

        if curr_max > global_max :
            global_max = curr_max

    return global_max


A = list(map(int, input().split()))
print(kadane(A))