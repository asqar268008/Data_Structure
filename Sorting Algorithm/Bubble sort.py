def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print("Bubble Sort")
arr = [42, 7, 91, 13, 58, 29, 73, 5, 64, 18, 37, 82, 26, 9, 51, 47, 33, 14, 69, 2]
print("Before Sorting\n",arr)
print("After Sorting\n",bubble_sort(arr))