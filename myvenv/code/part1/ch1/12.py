# https://www.acmicpc.net/problem/2164

# import sys
# from collections import deque

# num = int(sys.stdin.readline())
# dq = deque([])

# for i in range(1, num + 1):
#     dq.append(i)

# while(True):
#     if len(dq) == 1:
#         break

#     dq.popleft()
#     if len(dq) == 1:
#         break
    
#     n = dq.popleft()
#     dq.append(n)

# print(dq[0])   

import sys
from collections import deque

num = int(sys.stdin.readline())
d = deque(list(range(1, num + 1)))
drop = True

while len(d) > 1:
    if drop:
        d.popleft()
        drop = False
    else:
        temp = d.popleft()
        d.append(temp)
        drop = True

print(d[0])        