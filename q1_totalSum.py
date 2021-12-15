def totalSum(x):
    sum = 0 # initialize sum var
    # iterate through n digits starting from 0 up to x (x+1 excluded)
    for i in range(x+1): 
        sum = sum + i # find sum of all digits 
    return sum

print(totalSum(8)) # print result