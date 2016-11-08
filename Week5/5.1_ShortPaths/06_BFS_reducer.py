import sys
INF = 10**10


def reducer(nid, dists, structs):
    d_min = INF
    for dist in dists:
        if dist != 'INF':
            d_min = min(int(dist), d_min)
    if d_min == INF:
        d_min = 'INF'

    m = '{}'
    for struct in structs:
        if struct != '{}':
            m = struct
            break

    print('{}\t{}\t{}'.format(nid, d_min, m))


def main():
    [last_key, cur_dists] = [None, []]
    struct = set()


    for line in sys.stdin:
        [key, dist, adj_list] = line.strip().split()
        if last_key and last_key != key:
            reducer(last_key, cur_dists, struct)
            struct.clear()
            struct.add(adj_list)
            cur_dists = [dist]
        else:
            cur_dists.append(dist)
            struct.add(adj_list)

        last_key = key

    if last_key:
        reducer(last_key, cur_dists, struct)



if __name__ == '__main__':
    main()