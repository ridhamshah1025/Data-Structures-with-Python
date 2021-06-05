def arr_sort(arr):
    lo = 0
    mid=0
    high=len(arr)-1
    while mid <= high:
        print(arr,lo,mid,high)
        if arr[mid] == 0:
            arr[lo],arr[mid] = arr[mid],arr[lo]
            lo+=1
            mid+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high = high-1
        # print(arr,lo,mid,high)

arr_sort([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])