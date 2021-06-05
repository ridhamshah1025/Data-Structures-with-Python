"""
Given an array arr of integer elements, the task is to find the range and coefficient of range of the given array where: 
Range: Difference between the maximum value and the minimum value in the distribution. 
Coefficient of Range: (Max – Min) / (Max + Min).

"""

def find_rangeand_coefficinet(arr):
    _min=arr[0]
    _max=arr[0]
    for i in range(2,len(arr)):
        if arr[i] < _min:
            _min = arr[i]
        if arr[i] > _max:
            _max = arr[i]
    print(_min)
    print(_max)
    _range=_max-_min
    _coeff = (_max-_min)/(_max+_min)
    print(_range,_coeff)

find_rangeand_coefficinet([15, 16, 10, 9, 6, 7, 17])