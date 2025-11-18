def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print("Insertion Sort")
arr = [42, 7, 91, 13, 58, 29, 73, 5, 64, 18, 37, 82, 26, 9, 51, 47, 33, 14, 69, 2]
print("Before Sorting\n",arr)
print("After Sorting\n",insertion_sort(arr))