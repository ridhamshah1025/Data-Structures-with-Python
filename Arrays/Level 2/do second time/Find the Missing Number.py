def getMissingNo(A):
    n = len(A)+1
    total = (n)*(n + 1)/2
    sum_of_A = sum(A)
    print(total,sum_of_A)
    return total - sum_of_A

# Driver program to test the above function
A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)