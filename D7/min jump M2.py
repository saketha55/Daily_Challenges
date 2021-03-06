#Method 2

def minJumps(arr, n):
    jumps = [0 for i in range(n)]
 
    if (n == 0) or (arr[0] == 0):
        return float('inf')
 
    jumps[0] = 0

    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]
 

arr = [1, 3, 6, 1, 0, 9]
arr2 = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
size = len(arr)
print('1.Minimum number of jumps to reach',
      'end is', minJumps(arr, size))
n=len(arr2)
print('2.Minimum number of jumps to reach',
      'end is', minJumps(arr2, n))
