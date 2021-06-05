def longestConsecutive(a):
    a = set(a)
    print(a)
    longest = 0
    for i in a:
        print(i-1)
        if i-1 not in a:
            # current = i
            streak = 0
            while i in a:
                print(i)
                i+=1
                streak+=1
                longest = max(longest,streak)
    return longest

print(longestConsecutive([100,4,250,1,3,2]))