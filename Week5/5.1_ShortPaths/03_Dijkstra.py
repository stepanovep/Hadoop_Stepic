import queue

INF = 1000 * 1000 * 1000 * 1000


def dijkstra(graph, w, n, s, t):
    d = [INF] * (n+1)
    visited = [False] * (n + 1)
    d[s] = 0

    q = queue.PriorityQueue()
    q.put((d[s], s))

    while not q.empty():
        u = q.get()[1]
        visited[u] = True
        min_cost = INF
        min_cost_id = 0
        for v in graph[u]:
            if d[v] > d[u] + w[u, v] and not visited[v]:
                d[v] = d[u] + w[u, v]
                if d[v] < min_cost:
                    min_cost = d[v]
                    min_cost_id = v

        if min_cost < INF:
            q.put((min_cost, min_cost_id))

    return d


def main():
    n, m = map(int, input().split())
    graph = {}
    w = {}
    for i in range(1, n+1):
        graph[i] = []

    for j in range(m):
        u, v, cost = map(int, input().strip().split())
        w[(u, v)] = cost
        graph[u].append(v)

    s, t = map(int, input().split())

    dist = dijkstra(graph, w, n, s, t)
    if dist[t] < INF:
        print(dist[t])
    else:
        print(-1)


if __name__ == '__main__':
    main()
