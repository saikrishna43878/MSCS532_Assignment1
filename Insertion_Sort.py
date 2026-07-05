arr = [15, 3, 22, 7, 9, 14]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] > arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
print("Sorted Array :",arr)
