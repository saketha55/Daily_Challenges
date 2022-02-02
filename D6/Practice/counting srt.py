# linear sorting

# COUNTING Sort:

arr=[2,4,1,6,3,5,9,8,7]
low,high=int(input("enter the range a to b:").split())
extra=[0]*(high-low+1)
n=len(arr)

for i in arr:
    extra[i]+=1
for i in range(1,len(extra)):
    extra[i]+=extra[i-1]


