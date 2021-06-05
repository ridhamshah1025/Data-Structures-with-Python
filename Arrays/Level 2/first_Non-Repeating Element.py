def find_first_non_duplicate(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            del dic[arr[i]]
            # dic[arr[i]] += 1
            # res.append(arr[i])
    print(list(dic.keys())[0])

find_first_non_duplicate([9 ,4 ,9 ,6 ,7 ,4])