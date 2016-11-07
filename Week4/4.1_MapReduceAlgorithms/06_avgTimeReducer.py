import sys


def main():

    [lastKey, curSum, cnt] = [None, 0, 0]

    for line in sys.stdin:
        [key, value] = line.strip().split()
        value = int(value)
        if lastKey and lastKey != key:
            print(lastKey, curSum // cnt, sep='\t', end='\n')
            curSum = value
            cnt = 1
        else:
            curSum += value
            cnt += 1

        lastKey = key

    if lastKey:
        print(key, curSum // cnt, sep='\t')


if __name__ == '__main__':
    main()
