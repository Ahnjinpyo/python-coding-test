# 배열 합치기
# https://www.acmicpc.net/problem/11728

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

posA = 0
posB = 0

while posA < N and posB < M:
    if A[posA] <= B[posB]:
        C.append(A[posA])
        posA += 1
    else:
        C.append(B[posB])
        posB += 1
        
# if posA < N:
#    C.extend(A[posA:N])
# else:
#     C.extend(B[posB:M])
if posA != N:
    C.extend(A[posA:N])
if posB != M:
    C.extend(B[posB:M])

# 결과 리스트의 요소들을 공백으로 구분하여 출력
print(*C)
 


