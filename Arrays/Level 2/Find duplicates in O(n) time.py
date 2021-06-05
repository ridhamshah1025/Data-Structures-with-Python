def find_duplicate(arr):
    dic = {}
    res = []
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1
            res.append(arr[i])
    print(dic,res)

find_duplicate([1, 2, 3, 6, 3, 6, 1])