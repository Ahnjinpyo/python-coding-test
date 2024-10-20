# 수들의 합
# https://www.acmicpc.net/problem/2003

import sys 
input = sys.stdin.readline

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

startIdx = 0
endIdx = 0
sum = A[startIdx]
count = 0
        
while True:
    if endIdx == N:
        break
    
    if sum < M:
        endIdx += 1
        if endIdx >= N:
            break
        sum += A[endIdx]
    elif sum == M:
        count += 1
        startIdx += 1
        sum -= A[startIdx - 1]
    elif sum > M:
        startIdx += 1
        sum -= A[startIdx - 1]
        
print(count)         
            
        