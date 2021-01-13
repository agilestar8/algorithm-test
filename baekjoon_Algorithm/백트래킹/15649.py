# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

from itertools import permutations

n,m = map(int,input().split())

p = permutations(range(1,n+1), m)

for i in p:

    print(" ".join(map(str,i)))
