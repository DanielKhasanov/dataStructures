def quickSort(arr):

    def __partition(arr, left, right):

        # First element is pivot
        pivot = arr[left]

        startingIndex = left + 1
        endingIndex = right

        done = False

        while not done:
            # Move left index along
            while startingIndex <= endingIndex and arr[startingIndex] <= pivot:
                startingIndex += 1
            # Move right index along
            while endingIndex >= startingIndex and arr[endingIndex] >= pivot:
                endingIndex -= 1
            # Escape clause
            if startingIndex > endingIndex:
                done = True
            # Swap left and right
            else:
                print("Swapping ", arr[startingIndex], " ", arr[endingIndex])
                arr[startingIndex], arr[endingIndex] = arr[endingIndex], arr[startingIndex]

        # Swap pivot with new midpoint to finish
        arr[left], arr[endingIndex] = arr[endingIndex], arr[left]
        return endingIndex



    def __quickSort (arr, left, right):
        # Left - Starting Index
        # Right - Ending Index
        if left < right:
            pi = __partition(arr, left, right)

            __quickSort(arr, 0, pi - 1)
            __quickSort(arr, pi + 1, right)

    __quickSort(arr, 0, len(arr) - 1)


testArr = [123, -123, 12, 34, 9, 342, 9002, -243, 3434, 7, 44.5, 24, 234]

print(testArr)

quickSort(testArr)

print(testArr)

## Extra Challenge: Median of Three Implementation