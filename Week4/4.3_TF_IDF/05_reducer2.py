import sys

def reducer(key, values):
    cnt = values.__len__()
    for value in values:
        docnum, tf, temp = value.split(';')
        print('{}#{}\t{}\t{}'.format(key, docnum, tf, cnt))


def main():
    last_key = None
    t = []
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        if last_key and key != last_key:
            reducer(last_key, t)
            t = [value]
        else:
            t += [value]
        last_key = key

    if last_key:
        reducer(last_key, t)

if __name__ == '__main__':
    main()
