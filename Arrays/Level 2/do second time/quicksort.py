def quicksort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pi = arr.pop()
        large = []
        small = []
        for i in range(len(arr)):
            if arr[i] < pi:
                small.append(arr[i])
            else:
                large.append(arr[i])
        return quicksort(small) + [pi] + quicksort(large)

print(quicksort([10, 80, 30, 90, 40, 50, 70]))
        
        