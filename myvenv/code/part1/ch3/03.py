import sys
input = sys.stdin.readline

N, K, B = list(map(int, input().split()))
broken = [0] * N

for i in range(B):
    brokenIdx = int(input()) - 1
    broken[brokenIdx] = 1
    
psum = [0] * N
psum[0] = broken[0]

for i in range(1, N):
    psum[i] = psum[i - 1] + broken[i]
    
    
min_broken = []
for i in range(N - K + 1):
    if i == 0:
        broken_count = psum[K - 1]
    else:
        broken_count = psum[K - 1 + i] - psum[i - 1]

    min_broken.append(broken_count)
    
print(min(min_broken))

