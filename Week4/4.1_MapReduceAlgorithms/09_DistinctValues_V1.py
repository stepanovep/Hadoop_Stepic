import sys


def mapperV1(line):
    h = []
    value, groups = line.strip().split()
    value = int(value)
    groups = groups.split(',')

    for group in groups:
        key = "{},{}".format(value, group)
        h += [key]

    return h


def reducerV1(text):
    lastkey = None
    for line in text:
        key, value = line.strip().split()
        if lastkey and key != lastkey:
            print(lastkey)
        else:
            pass

        lastkey = key

    if lastkey:
        print(lastkey)


def main():
    H = []
    for line in sys.stdin:
        H += mapperV1(line)

    for key in H:
        print(key, 1, sep='\t')


if __name__ == '__main__':
    main()
