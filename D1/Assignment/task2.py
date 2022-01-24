#Question 2
# Print each node's data element, one per line, given a pointer to the head node of a linked list.
# There is nothing to output if the head reference is null (meaning the list is empty).

#Complete the  printlinkedlist function:
def printlinkedlist(head):
    if head==Null:
        print("linked list is empty")
        return
    while head.next!=Null:
        print(head.data)
        head=head.next
    return
