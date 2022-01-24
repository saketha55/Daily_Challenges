#basic:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail =new_node
            return
        self.tail.next=new_node
        self.tail=new_node

    def getNode(self,value):
        curr_node=self.head
        while(curr_node.next and curr_node.data != value):
            curr_node=curr_node.next
        if(curr_node.data==value):
            return curr_node
        else:
            return None

    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')


#Delete without head pointer
#https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1
def deleteNode(self,curr_node):

        temp=curr_node.next
        curr_node.data= temp.data
        curr_node.next=temp.next
        temp=None

t=int(input())
for cases in range(t):
    n = int(input())
    a = LinkedList() # create a new linked list 'a'.
    nodes = list(map(int, input().strip().split()))
    for x in nodes:
        a.append(x)
    del_elem = int(input())
    to_delete=a.getNode(del_elem)
    Solution().deleteNode(to_delete)
    a.printList()
