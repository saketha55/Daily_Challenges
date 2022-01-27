#Implement Queeue using Stack:

st1=[]
st2=[]

def enqueue(x):
    while len(st1)!=0:
        t=st1.pop()
        st2.append(t)
    st1.append(x)
    while len(st2)!=0:
        st1.append(st2.pop())
    display()
def dequeue():
    if len(st1)==0:
        print("underflow detected")
        return
    else:
        st1.pop()
    display()
def display():
    print("actual queue:",st1)
    #print("extra:" , st2)
    
enqueue(5)
enqueue(3)
enqueue(8)
enqueue(56)
dequeue()
enqueue(9)
print("Final:")
display()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
