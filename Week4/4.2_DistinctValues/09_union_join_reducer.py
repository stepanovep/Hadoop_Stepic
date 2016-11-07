import sys

def reducer(key, t):
    query = []
    url = []
    for str in t:
        opt, value = str.split(':')
        if opt == 'query':
            query.append(value)
        else:
            url.append(value)

    for q in query:
        for u in url:
            print('{}\t{}\t{}'.format(key, q, u))



def main():
    last_key = None

    t = []
    for line in open('in.txt', 'r'):
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
