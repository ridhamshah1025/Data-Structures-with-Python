def check_array(arr,n,b):

    length = len(arr)
    loop_round = length//b
    if length%b==0:
        loop_round = length//b
    else:
        loop_round = (length//b) + 1
    print(length, loop_round)
    for i in range(loop_round):
        block = arr[(i*b):(b*(i+1))]
        if n in block:
            if i == loop_round:
                return True
        else:
            return False

arrr = [5, 8, 7, 12, 14, 3, 9]
x = check_array(arrr,8,2)
if x == False:
    print("No")
else:
    print("Yes")