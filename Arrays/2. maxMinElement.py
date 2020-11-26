a = list(map(int, input().split()))

min = 0
max = 0
length = len(a)

for i in range(length):
    if a[i] < a[min]:
        min = i
    
    if a[i] > a[max]:
        max = i
    
print("Minimum = " + str(a[min]))
print("Maximum = " + str(a[max]))
