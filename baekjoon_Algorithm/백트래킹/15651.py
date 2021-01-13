from itertools import product

n,m = map(int,input().split())

arr = list(range(1,n+1))

for i in product(arr, repeat=m):
    print(" ".join(map(str,i)))

