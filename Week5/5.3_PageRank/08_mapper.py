import sys


def mapper(line):
    print(line)
    v, p, adj = line.strip().split()
    adj = adj[1:-1].replace(',', ' ').split()

    for u in adj:
        print('%s\t%.3f\t%s' % (u, float(p) / adj.__len__(), '{}'))


def main():
    for line in sys.stdin:
        mapper(line.strip())


if __name__ == '__main__':
    main()
