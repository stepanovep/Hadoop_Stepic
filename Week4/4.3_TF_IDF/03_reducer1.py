import sys

def reducer(key, value):
    key, id = key.split('#')
    print('{}\t{}\t{}'.format(key, id, value))



def main():
    last_key, t = None, 0
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        value = int(value)
        if last_key and key != last_key:
            reducer(last_key, t)
            t = value
        else:
            t += value
        last_key = key

    if last_key:
        reducer(last_key, t)

if __name__ == '__main__':
    main()
