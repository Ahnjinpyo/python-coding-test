# 신입 사원
# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

T = int(input())    # 테스트 케이스 입력

for _ in range(T):  # 원소 접근이 불필요 하기 때문에 _ 로 loop 선회
    N = int(input())    # 지원자 입력        
    
    candidates = []
    target = 0
    standard_ranking = 1e6  
    
    for _ in range(N):
        s, m = map(int, input().split())
        candidates.append((s, m))
        
    candidates.sort()
    
    for i in range(N):
        if candidates[i][1] < standard_ranking:
            standard_ranking = candidates[i][1]
            target += 1
    
    print(target)
        
# 이문제의 핵심 포인트는 시간 복잡도다 
# 2차원 배열로 순위가 기록되어 있는 배열에서 첫번째 원소 기준으로 정렬을 한 뒤에 
# 각 행의 두번째 원소를 앞전의 원소와 비교해 보면서 
# 비교 대상이 되는 행의 위에 있는 모든 행을 비교해 보는게 아니라 
# 높은 순위가 있을 때 마다 갱신을 하고 그 순위와 비교대상을 비교만 해보면 되니 복잡도가 훨씬 낮아진다        