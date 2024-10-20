import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
T = list(map(int, input().split()))

psum = [0] * N
psum[0] = T[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + T[i]

temp_sum = []
sum = 0
for i in range(0, N - K + 1):
    if i == 0:
       sum = psum[i + K -1]
    else:
        sum = psum[i + K - 1] - psum[i - 1]

    temp_sum.append(sum)

print(max(temp_sum))