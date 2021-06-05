def findPair(A, sum):
 
    # consider each element except the last
    for i in range(len(A) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(A)):
 
            # if the desired sum is found, print it
            if A[i] + A[j] == sum:
                print("Pair found", (A[i], A[j]))
                return
 
    # No pair with the given sum exists in the list
    print("Pair not found")
 
 
if __name__ == '__main__':
 
    A = [8, 7, 2, 5, 3, 1]
    sum = 10
 
    findPair(A, sum)

def getPairsCount(arr, n, sum):
 
    m = [0] * 1000
 
    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
    
    # print(m)
 
    twice_count = 0
 
    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):
        # print(m[sum-arr[i]])
        twice_count += m[sum - arr[i]]

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twice_count
    return int(twice_count / 2)
# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6

print("Count of pairs is", getPairsCount(arr,n, sum))



def findPair(A, sum):
 
    # create an empty dictionary
    dict = {}
 
    # do for each element
    for i, e in enumerate(A):
        print(i,e)
        print(dict)
        # check if pair `(e, sum - e)` exists
 
        # if the difference is seen before, print the pair
        if sum - e in dict:
            print("Pair found", (A[dict.get(sum - e)], A[i]))
 
        # store index of the current element in the dictionary
        dict[e] = i
 
    # No pair with the given sum exists in the list
    print("Pair not found")
 
 
if __name__ == '__main__':
 
    A = [8, 7, 2, 5, 3, 1]
    sum = 10
 
    findPair(A, sum)