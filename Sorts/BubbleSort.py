def bubbleSort(arr):
    lastIndex = len(arr)
    earlyExit = False
    # Slice of list to sort
    while lastIndex > 0 and not earlyExit:
        # Swap until end of list
        for index in range(lastIndex - 1):
            if arr[index] >= arr[index + 1]:
                # Swap
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                earlyExit = False
            else:
                earlyExit = True
        lastIndex -= 1
    print("Early Exit: ", earlyExit, " | ", len(arr) - lastIndex, " Passes")


testList = [12312, 2, 33, 52, 133, 965, 123, 768, 23, 86]
print(testList)
bubbleSort(testList)
print(testList, "\n\n")

print(testList)
bubbleSort(testList)
print(testList)