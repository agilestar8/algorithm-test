# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

n, edge = map(int,input().split())
start_node = int(input())
graph = [[] for i in range(n+1)]

for i in range(edge):
    a,b,c = map(int,input().split())    
    graph[a].append((b,c))

distance = [inf] * (n+1)


def dijkstra(start_node):
    queue = []

    heapq.heappush(queue, (0, start_node))
    distance[start_node] = 0

    while queue:
        dist, now_node = heapq.heappop(queue)

        if distance[now_node] < dist:
            continue
        
        for i in graph[now_node]:
            cost = dist + i[0]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start_node)

for i in range(1, n+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
    
