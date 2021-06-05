def find_min(arr):
    new_min = arr[0]
    for i in range(len(arr)):
        new_min = min(new_min,arr[i])
    print(new_min)
    
def find_max(arr):
    new_max = arr[0]
    for i in range(len(arr)):
        new_max = max(new_max,arr[i])
    print(new_max)

# arr = [1,2,3,4,5]
arr = [12, 1234, 45, 67, 1]
find_min(arr)
find_max(arr)


"""

Recursive program

"""    
# Python3 program to find minimum
# (or maximum) element in an array.
def getMin(arr, n):
    if(n==1):
        return arr[0]
    # If there is single element, return it.
    # Else return minimum of first element
    # and minimum of remaining array.
    else:
        return min(getMin(arr[1:], n-1), arr[0])
def getMax(arr, n):
    if(n==1):
        return arr[0]
    # If there is single element, return it.
    # Else return maximum of first element
    # and maximum of remaining array.
    else:
        return max(getMax(arr[1:], n-1), arr[0])
# Driver code
arr = [12, 1234, 45, 67, 1]
n = len(arr)
print("Minimum element of array: ",getMin(arr, n))
print("Maximum element of array: ",getMax(arr, n))