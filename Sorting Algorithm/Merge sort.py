def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0 #indices for L, R and arr

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

print("Merge Sort")
arr = [42, 7, 91, 13, 58, 29, 73, 5, 64, 18, 37, 82, 26, 9, 51, 47, 33, 14, 69, 2]
print("Before Sorting\n",arr)
print("After Sorting\n",merge_sort(arr))