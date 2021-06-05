"""algo for GCD
def gcd(x,y)
    if x==0:
        return y
    if y==0
        return x
    return gcd(b,a%b)
"""
def gcd(x,y):
    if x==0:
        return y
    if y==0:
        return x
    return gcd(y,x%y)

def find_gcd(arr,x,y):
    temp = arr[x]
    for i in range(x+1,y+1):
        temp = gcd(temp,arr[i])
    print(temp)

find_gcd([2, 3, 60, 90, 50],2,4)