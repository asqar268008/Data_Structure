def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("Selection Sort")
arr = [42, 7, 91, 13, 58, 29, 73, 5, 64, 18, 37, 82, 26, 9, 51, 47, 33, 14, 69, 2]
print("Before Sorting\n",arr)
print("After Sorting\n",selection_sort(arr))