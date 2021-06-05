def find_first_duplicate(arr):
    dic = {}
    res = []
    for i in range(len(arr)-1,-1,-1):
        # print(arr[i])
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            Min = i
            dic[arr[i]] += 1
            res.append(arr[i])
            # print(dic,arr[i],res)
    print(arr[Min])
    for i,j in dic.items():
        if j >= 2:
            # print(i)
            break

find_first_duplicate([6, 10, 5, 4, 9, 120, 4, 6, 10])
