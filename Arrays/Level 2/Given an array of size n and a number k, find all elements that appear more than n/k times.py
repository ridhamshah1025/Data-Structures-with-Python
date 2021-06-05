def find_number_for_n_divide_k_times(arr, k):
    dic = {}
    n = len(arr)
    for i in range(len(arr)):
        if arr[i] not in dic.keys():
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1
    for i,j in dic.items():
        if j > (n//k):
            print(i)

find_number_for_n_divide_k_times([3, 1, 2, 2, 1, 2, 3, 3],4)