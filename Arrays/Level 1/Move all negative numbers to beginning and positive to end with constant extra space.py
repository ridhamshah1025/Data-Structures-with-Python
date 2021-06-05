def move_all_elements_positive_and_negative(arr):
    start=0
    high=len(arr)-1
    while start <= high:
        if arr[start] < 0:
            start+=1
        else:
            arr[start],arr[high] = arr[high],arr[start]
            high-=1
    print(arr)

move_all_elements_positive_and_negative([-12, 11, -13, -5, 6, -7, 5, -3, -6])        