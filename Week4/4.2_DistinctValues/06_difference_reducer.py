import sys


def reducer(t, n):
    if n == ['A']:
        print(t)


def main():
    last_key = None
    n = []
    for line in open('in.txt', 'r'):
        key, value = line.strip().split()
        if last_key and key != last_key:
            reducer(last_key, n)
            n = [value]
        else:
            n += [value]
        last_key = key

    if last_key:
        reducer(last_key, n)


if __name__ == '__main__':
    main()


#У всех задач 95% общего кода, меняется лишь строка (пара строчек)в методе reducer(value t, array n)