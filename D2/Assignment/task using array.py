# You have an empty sequence, and you will be given
# queries. Each query is one of these three types:
# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.


def push(x):
    global extra,stck
    stck.append(x)
        #top+=1
    if isEmpty(extra):
        extra.append(x)
    if x >= extra[-1]:
        extra.append(x)

def pop():
    global extra,stck
    if stck[-1]==extra[-1]:
        extra.pop()

    if isEmpty(stck):
        print("Underflow Detected")
    else:
        stck.pop()
        #top-=1

def isEmpty(s):
    return len(s)==0

def maximun():
    return extra[-1]


stck=[]
extra=[]

Testcase=int(input())
i=0
for i in range(Testcase):
    a=list(map(int,input().split()))
    if a[0]==1:
        push(a[1])
    if a[0]==2:
        pop()
    if a[0]==3:
        print(maximun())
for i in range(len(stck)):
    print(stck[i], end=" ")
