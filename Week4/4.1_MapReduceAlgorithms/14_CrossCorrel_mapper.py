import sys


def mapper(elements):
    for i in elements:
        for j in elements:
            if i != j:
                print("{},{}\t1".format(i, j))


def main():
    for line in open('in.txt', 'r'):
        mapper(line.strip().split())

if __name__ == '__main__':
    main()