# O(n) time | O(1) space
# entirely non-decreasing or entirely non-increasing
def isMonotonic(arr):
    if len(arr) <= 2:
        return True

    direction = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i-1]
            continue

        if breaksDirection(direction, arr[i]-arr[i-1]):
            return False

    return True


def breaksDirection(direction, difference):
    if direction > 0:
        return difference < 0
    return difference > 0


def isMonotonic_Aternate(arr):
    isNonInc = True
    isNonDec = True

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 0:
            isNonInc = False
        if arr[i] - arr[i-1] < 0:
            isNonDec = False

    return isNonDec or isNonInc


# Driver
arr = [1, 2, 2, 3, 2, 5]
print(isMonotonic(arr))
print(isMonotonic_Aternate(arr))
