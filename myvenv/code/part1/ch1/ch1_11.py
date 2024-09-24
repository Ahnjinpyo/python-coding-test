
# https://www.acmicpc.net/problem/18258

# queue = []
# count = int(input())

# for i in range(count):
#     command = input()
    
#     if command.startswith("push"):
#         num = command.split(' ')[1]
#         queue.append(num)

#     if command == "pop":
#         print(queue.pop(-1))

#     if command == "size":
#         print(len(queue))

#     if command == "empty":
#         if (len(queue) > 0):
#             print(0)
#         else:
#             print(1)
    
#     if command == "front":
#         if (len(queue) == 0):
#             print(-1)
#         else:
#             print(queue(-1))
    
#     if command == "back":
#         if (len(queue) == 0):
#             print(-1)
#         else:
#             print(queue(len(queue)))

import sys
from collections import deque

count = int(input())
dq = deque([])

for i in range(count):
    command = sys.stdin.readline()
    command = command.split()

    if (command[0] == "push"):
        dq.append(int(command[1]))

    if (command[0] == "pop"):
        if (len(dq) == 0):
            print(-1)
        else:
            print(dq.popleft())

    if (command[0] == "size"):
        print(len(dq))

    if (command[0] == "empty"):
        if (len(dq) == 0):
            print(1)
        else:
            print(0)

    if (command[0] == "front"):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    
    if (command[0] == "back"):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    

