def find_frequancy(arr,k):
    count = 0
    for i in range(len(arr)):
        if arr[i] == k:
            count+=1
    print(count)

find_frequancy([0, 5, 5, 5, 4],5)

find_frequancy([1,2,3],4)
