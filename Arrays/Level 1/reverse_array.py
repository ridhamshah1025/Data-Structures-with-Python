def reverse_array(arr):
    r_list = []
    length = len(arr)
    # print(length)
    # for i in range(10,0,-1):
    #     print(i)
    for i in range(len(arr),0,-1):
        # print(arr[i-1])
        # r_list = r_list.append(arr[i])
        r_list.append(arr[i-1])
    print(r_list)

reverse_array([5,4,3,2])