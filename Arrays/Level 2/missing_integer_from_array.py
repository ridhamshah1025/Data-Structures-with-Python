def find_miss_integer(arr):
    total = 0
    for i in range(1,len(arr)+2):
        total+=i
        if i < len(arr)+1:
            total-=arr[i-1]
    print(total)

find_miss_integer([1,2,3,4])