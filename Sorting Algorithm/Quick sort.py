def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
print("Quick Sort")
arr = [42, 7, 91, 13, 58, 29, 73, 5, 64, 18, 37, 82, 26, 9, 51, 47, 33, 14, 69, 2]
print("Before Sorting\n",arr)
print("After Sorting\n",quick_sort(arr))