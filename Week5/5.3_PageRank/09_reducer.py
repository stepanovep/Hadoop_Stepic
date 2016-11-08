import sys
alpha = 0
N = 5

def reducer(nid, structs):
    s = alpha / N
    m = '{}'
    for struct in structs:
        if struct[1] != '{}':
            m = struct[1]
        else:
            s += (1-alpha)*struct[0]

    print('{}\t{:.4f}\t{}'.format(nid, s, m))


def main():
    last_key = None
    struct = []

    for line in sys.stdin:
        [key, p, adj_list] = line.strip().split()
        key = int(key)
        p = float(p)
        if last_key and last_key != key:
            reducer(last_key, struct)
            struct = [(p, adj_list)]

        else:
            struct.append((p, adj_list))

        last_key = key

    if last_key:
        reducer(last_key, struct)


if __name__ == '__main__':
    main()