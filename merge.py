def merge_sort(arr):
    """
 -- recursively sort 1st half of the input array
 -- recursively sort 2nd half of the input array
 -- merge two sorted sublists into one
[ignores base cases]
!! No OUTPUT LIST 
    a = 1st half 
    b = 2nd half
    """
    if len(arr) > 1:
        half = len(arr) // 2
        a = arr[:half]
        b = arr[half:]
        merge_sort(a)
        merge_sort(b)

        i = j = k = 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                arr[k] = a[i]
                i += 1
            else :
                arr[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            arr[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            arr[k] = b[j]
            j += 1
            k += 1
    return arr
        
arr = [12, 11, 13, 5, 6, 7, 5, 8, 21, 99, 50, 3]
print("Before :")
print(arr)
print("After :")
merge_sort(arr)
print(arr)


