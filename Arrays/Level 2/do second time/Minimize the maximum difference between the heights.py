def find_min_height_frommax_height_diff(arr,k):
    arr.sort()
    n = len(arr)
    ans = arr[n-1] - arr[0]
    smallest_tower = arr[0] + k 
    longest_tower = arr[n-1]-k
    for i in range(len(arr)-1):
        mi = min(smallest_tower,arr[i+1]-k)
        mx = max(longest_tower,arr[i]+k)
        ans = min(ans,mx-mi)
    print(ans)

find_min_height_frommax_height_diff([1, 15, 10],6)
