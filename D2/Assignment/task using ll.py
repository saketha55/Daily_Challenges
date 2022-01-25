class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class operations:

    def __init__(self):
        self.root = None

    def push(self, data):

        newNode = Node(data)
        newNode.next = self.root
        self.root = newNode

        global extra
        if len(extra)==0:
            extra.append(data)
        if data >= extra[-1]:
            extra.append(data)

    def pop(self):
        if (self.isEmpty()):
            return float("Underflow detected")
        temp = self.root
        self.root = self.root.next
        popped = temp.data

        global extra
        if popped==extra[-1]:
            extra.pop()

    def isEmpty(self):
        if self.root is None:
            return True
        return False

    def display(self):
        track=self.root
        while track!=None:
            print(track.data, end=" ")
            track=track.next

    def maxnum(self):
        print(extra[-1])

stck=operations()
Testcase=int(input())
i=0
extra=[]
for i in range(Testcase):
    a=list(map(int,input().split()))
    if a[0]==1:
        stck.push(a[1])
    if a[0]==2:
        stck.pop()
    if a[0]==3:
        stck.maxnum()
stck.display()
