#method 2:

st1=[]
st2=[]

def enqueue(x):
    st1.append(x)
    display()
def dequeue():
    if len(st1)==0 and len(st2)==0:
        print("underflow detected")
        return
    elif len(st1)>0 and len(st2)==0:
        while len(st1):
            temp= st1.pop()
            st2.append(temp)
        return st2.pop()
    else:
        return st2.pop()
    #display()
def display():
    print("actual queue:",st1)
    print("popping queue:",st2)
    #print("extra:" , st2)
    
enqueue(5)
enqueue(3)
enqueue(8)
enqueue(56)
print("popped value is: ",dequeue())
enqueue(9)
print("popped value is: ",dequeue())
print("Final:")
print("stack 1: ",st1)
print("stack 2: ",st2)
