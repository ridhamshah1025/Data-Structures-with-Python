def rearrange(arr, n):
    # sort the array
    arr.sort()

    # initialize two pointers
    # one pointing to the negative number
    # one pointing to the positive number
    i, j = 1, 0
    while j < n:
        if arr[j] >= 0:
            break
        j += 1
    print(i, j, arr[0])
    # swap the numbers until the given condition gets satisfied
    while (arr[i] < 0) and (j < n):
        print(arr[i])
        # swaping
        arr[i], arr[j] = arr[j], arr[i]

        # increment i by 2
        # because a negative number is followed by a positive number
        i += 2
        j += 1

    return(arr)


# Driver Code
# Given array
arr = [-5, -2, -1, -3, -4, -6, -7, -10, -11, 5, 2, 0, -8]
ans = rearrange(arr, len(arr))
for num in ans:
    print(num, end=" ")
