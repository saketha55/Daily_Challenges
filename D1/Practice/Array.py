#Sort an array of 0s, 1s and 2s
#https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
arr=[1,2,0,2,2,1,0,1]
arr2=[4,5,7,8,2,6,1,3]

def sort012(arr,n):
    front=0
    rear=n-1
    mid=0

    while mid<=rear:
        if arr[mid]==0:
            arr[front],arr[mid]=arr[mid],arr[front]
            front+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[rear],arr[mid]=arr[mid],arr[rear]
            rear-=1
    return arr
print(sort012(arr,len(arr)))


#Union of two arrays
#https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1
def union(a,b):
    #maxln=max(len(ar1),len(ar2))
    a.sort()
    b.sort()
    i,j = 0,0
    while (i < len(a) and j < len(b)):
        if (a[i] > b[j]):
            j += 1
        else:
            if (b[j] > a[i]):
    i = 0
    j = 0
    while (i < n and j < m):

        if (a[i] > b[j]):
            j += 1

        else:
            if (b[j] > a[i]):
                i += 1
            else:
                print(a[i], end=" ")
                i += 1
                j += 1

union(arr,arr2)


#Wave Array
#https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1
def convertToWave(arr,N):
    arr.sort()
    temp=0
    for i in range(1,N,2):
        temp=arr[i]
        arr[i]=arr[i-1]
        arr[i-1]=temp
    return arr
print(convertToWave(arr2,len(arr2)))
