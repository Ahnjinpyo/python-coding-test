# 예산
# https://www.acmicpc.net/problem/2512

# num = int(input())
# jibang = list(map(int, input().split()))
# budget = int(input())
#
# left = 0
# right = max(jibang)
# answer = -1
#
# while (True):
#     if left >= right:
#         break
#
#     middle = (left + right) // 2
#     sum = 0
#
#     for i in jibang:
#         sum += min(middle, i)
#
#     if sum < budget:
#         answer = middle
#         left = middle + 1
#     elif sum > budget:
#         right = middle - 1
#     else:
#         answer = middle
#
# print(answer)

num = int(input())
jibang = list(map(int, input().split()))
budget = int(input())

left = 0
right = max(jibang)
answer = -1

while left <= right:
    sum = 0
    middle = (left + right) // 2
    for i in range(num):
        sum += min(middle, jibang[i])

    if sum <= budget:
        answer = middle
        left = middle + 1
    else:
        right = middle - 1

print(answer)


