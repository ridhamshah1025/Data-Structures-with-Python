def find_kth_min_element(arr,k):
    for i in range(len(arr)):
        first = i
        for j in range(i+1,len(arr)):
            if arr[first] > arr[j]:
                first = j
        arr[i],arr[first] =arr[first],arr[i]
    print(arr[k])

find_kth_min_element([5,2,6,8,2,4,47],3-1)
find_kth_min_element([7, 10, 4, 3, 20, 15],3-1)
find_kth_min_element([7, 10, 4, 3, 20, 15],4-1)