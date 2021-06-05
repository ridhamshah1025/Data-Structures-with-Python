def selection_sort(arr):
    for i in range(len(arr)):
        first = i
        print(arr[first])
        for j in range(i+1, len(arr)):
            print(arr[j])
            if arr[first] > arr[j]:
                first = j
        arr[i], arr[first] =  arr[first],arr[i]
        print(arr)
    
    print(arr)

arr = [5,4,3,2]
selection_sort(arr)