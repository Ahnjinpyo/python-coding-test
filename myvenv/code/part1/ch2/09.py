# https://www.acmicpc.net/problem/10819
# 차이를 최대로

from itertools import permutations
import sys 
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

answer = 0

for part in permutations(A, N):
    part = list(part)
    sum = 0
    for i in range(N - 1):
        # a = part[i] - part[i+1]
        # if a < 0:
        #     a = a * -1
        # sum += a
        sum += abs(part[i] - part[i+1])
    if answer < sum:
        answer = sum
        
print(answer)        
    