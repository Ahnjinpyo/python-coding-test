# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이

from itertools import combinations
import sys 
input = sys.stdin.readline

heights = []
for _ in range(9):
    height = int(input())
    heights.append(height)

for part in combinations(heights, 7):    
    if sum(part) == 100:
        part = list(part)
        sorted_part = sorted(part)
        for i in sorted_part:
            print(i)
        break

# **combinations(heights, 7)**를 사용할 때, part는 각 조합의 튜플로 생성됩니다. 이 튜플은 한 번 사용하면 소모됩니다. 
# 따라서, sorted(part)를 호출하면 해당 튜플이 소모되어 이후에 접근할 수 없습니다.
# **part = list(part)**로 변환하면, 튜플을 리스트로 복사하여 이후에 계속 사용할 수 있게 됩니다.
# 그래서 **part = list(part)**가 없으면 sorted(part)가 빈 튜플을 참조하려고 해서 런타임 에러가 발생하게 됩니다.