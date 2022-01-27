#priority Queue:

import queue 

class PriorityQueue():
    def __init__(self):
        self.queue=[0]
    def put(self,data):
        self.queue.append(data)
    def get(self,*x):
        if not x:
            self.queue.pop()
        else:
            self.queue.pop()[x]

total_wait = 0
n=int(input())
available = queue.PriorityQueue()
t=[0]*n
for i in range(n):
    t[i]=list(map(int,input().split()))
#print(t)
t.sort(key=lambda x:x[0], reverse=True) #sort the list based on time of order in reverse order
#print(t)
last_order = t.pop()
#print("dss0: ",last_order)
last_order.append(last_order[0] + last_order[1])
#print("dss1: ",last_order)
total_wait += last_order[2] - last_order[0]
#print("dss2: ",total_wait)

time = last_order[2]
for _ in range(n-1):
                        
    while(t and time >= t[-1][0]):   #whyyyyyyy
        node = t.pop()
        available.put((node[1], node))
                        
    if available:
        deleted = available.get()[1]
        print("bug: ",deleted)
        deleted.append(time + deleted[1])
        total_wait += deleted[2] - deleted[0]
        last_order = deleted
    else:
        temp = t.pop()
        temp.append(temp[0] + temp[1])
        total_wait += temp[2] - temp[0]
        last_order = temp

    time = last_order[2]

    
print(total_wait//n)

