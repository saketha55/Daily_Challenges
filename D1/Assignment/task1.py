# Question 1
#
# Reverse an integer array.
# P=[4,5,6]
# Return [6,5,4]

#example case
arr=[4,5,6,8,9,12,158,18,45,25,13]
q=len(arr)

#method 1
print(arr[::-1])

#method 2
for i in range(q-1,-1,-1):
    print(arr[i], end=" ")
print()

#method 3
for i in range(q):
    print(arr[q-i-1], end=" ")
print()
