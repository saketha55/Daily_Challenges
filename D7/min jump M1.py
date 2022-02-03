# method 1

def minJumps(arr, low, high):  #(0,9),(1,9)

    if (high == low):          #same index
        return 0
 
    if (arr[low] == 0):        # starting itself deadend
        return float('inf')
    
    min = float('inf')
    for i in range(low + 1, high + 1):      #(1 to 10)
        if (i < low + arr[low] + 1):        # 1<2,2<5... 
            jumps = minJumps(arr, i, high)  #(1,9),(2,9),(3,9)...
            if (jumps != float('inf') and jumps + 1 < min):
                min = jumps + 1
 
    return min
 
arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
arr2= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)                                #10
print('1.Minimum number of jumps to reach',
     'end is', minJumps(arr, 0, n-1))
m=len(arr2)
print('2.Minimum number of jumps to reach',
     'end is', minJumps(arr2, 0, m-1))
#[2,3,1,2,0]=2
