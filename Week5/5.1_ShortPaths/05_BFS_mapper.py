import sys
import re


def mapper(line):
    print(line)
    v, dist, adj = line.strip().split()
    adj = adj[1:-1].replace(',', ' ').split()

    for u in adj:
        if dist != 'INF':
            print('{}\t{}\t{}'.format(u, int(dist)+1, '{}'))
        else:
            print('{}\t{}\t{}'.format(u, 'INF', '{}'))

def main():
    for line in sys.stdin:
        mapper(line.strip())


if __name__ == '__main__':
    main()
