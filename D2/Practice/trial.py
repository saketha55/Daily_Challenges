from queue import Queue

q = Queue(maxsize = 3)
print(q.qsize())

#pushing
q.put('art')
q.put('bat')
q.put('cat')

# print(q)

#popping
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
