def longestPeak(arr):
    longestPeakLength = 0
    arrayLength = len(arr)
    i = 1
    while i < arrayLength-1:
        isPeak = arr[i-1] < arr[i] > arr[i+1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and arr[leftIdx] < arr[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = i + 2
        while rightIdx < arrayLength and arr[rightIdx] < arr[rightIdx - 1]:
            rightIdx += 1

        currPeak = rightIdx - leftIdx - 1
        longestPeakLength = max(currPeak, longestPeakLength)

        i = rightIdx

    return longestPeakLength


arr = [1, 2, 3, 1, 0, 3, 4, 5, 4, 3]
print(longestPeak(arr))
