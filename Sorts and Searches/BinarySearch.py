def binarySearch(arr, target):

    startingIndex = 0
    lastIndex = len(arr) - 1
    found = False

    while startingIndex <= lastIndex and not found:
        midpoint = (startingIndex  + lastIndex) // 2
        if arr[midpoint] == target:
            found = True
        else:
            if arr[midpoint] > target:
                startingIndex = midpoint + 1
            else:
                lastIndex = midpoint - 1

    return found




