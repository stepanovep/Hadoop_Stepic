
INF = 10**10
edges = []


def Ford_Bellman(n, s, t):
    dist = [INF] * (n+1)
    dist[s] = 0
    for i in range(n):
        for e in edges:
            if dist[e[0]] < INF:
                if dist[e[1]] > dist[e[0]] + e[2]:
                    dist[e[1]] = dist[e[0]] + e[2]

    return dist


def main():
    n, m = map(int, input().split())
    for j in range(m):
        u, v, cost = map(int, input().split())
        edges.append([u, v, cost])

    s, t = map(int, input().split())

    dist = Ford_Bellman(n, s, t)
    if dist[t] < INF:
        print(dist[t])
    else:
        print(-1)


if __name__ == '__main__':
    main()
