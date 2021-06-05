def findMin(arr, low, high):

    while (low < high):
        mid = low + (high - low) // 2

        if (arr[mid] == arr[high]):  # this condition
            high -= 1
        elif(arr[mid] > arr[high]):
            low = mid + 1
        else:
            high = mid
    return arr[high]


# Driver code
if __name__ == '__main__':

    # arr1 = [3, 4,5,6,1,2]
    arr1 = [3]
    n1 = len(arr1)
    print("The minimum element is ",
          findMin(arr1, 0, n1 - 1))
