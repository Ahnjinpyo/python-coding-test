# 기타레슨
# https://www.acmicpc.net/problem/2343

N, M = map(int, input().split())
running_time = list(map(int, input().split()))

left = max(running_time)
right = sum(running_time)
answer = -1

while left <= right:
    mid = (left + right) // 2
    bluray_num = 1
    remain = mid

    for i in range(N):
        if remain < running_time[i]:
            bluray_num += 1
            remain = mid

        remain -= running_time[i]

    if bluray_num <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)