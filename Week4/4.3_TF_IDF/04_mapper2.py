import sys
import re


def mapper(key, value):
    num, tf = value.strip().split()
    print('{}\t{};{};{}'.format(key, num, tf, 1))


def main():
    for line in sys.stdin:
        key, value = line.strip().split('\t', 1)
        mapper(key, value)


if __name__ == '__main__':
    main()