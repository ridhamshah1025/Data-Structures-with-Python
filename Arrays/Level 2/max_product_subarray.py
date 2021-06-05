def max_pro_subarray(arr):
    _min = 1
    _max = 1
    __max = 1
    for i in range(len(arr)):
        if arr[i] == 0:
            _min=1
            _max=1
        elif arr[i] > 0:
            _max = arr[i]*_max
            _min = min(1,arr[i]*_min)
        else:
            temp = _max
            _max = max(arr[i]*_min,temp)
            _min = min (arr[i]*temp,1)
        if __max < _max:
            __max = _max
    print(__max)

max_pro_subarray([6, -3, -10, 0, 2])