

def max_product_subarray(arr):
    max_pro = 1
    min_pro = 1
    max_so_far = 0
    for i in range(len(arr)):
        print(max_pro,min_pro,max_so_far,i)
        if arr[i] > 0:
            max_pro = max_pro*arr[i]
            min_pro = min(min_pro*arr[i],1)
        elif arr[i] ==0:
            max_pro = 1
            min_pro = 1
        else:
            temp = max_pro
            max_pro = max(min_pro*arr[i],1)
            min_pro = temp*arr[i]
        if (max_so_far < max_pro):
            max_so_far = max_pro
    return max_so_far
        # current_pro = max(arr[i],(arr[i]*current_pro))
        # max_pro = max(current_pro,max_pro)

print(max_product_subarray([6, -3, -10, 0, 2]))
