import itertools 

pockets = [1, 2, 3, 4]

# 조합
print(list(itertools.combinations(pockets, 2)))

# 순열
print(list(itertools.permutations(pockets, 2)))

# 부분집합
subset = []
for i in range(len(pockets) + 1):
    subset.extend(list(itertools.combinations(pockets, i)))
    
print(subset)    
