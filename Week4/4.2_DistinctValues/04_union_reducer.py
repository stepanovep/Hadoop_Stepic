import sys


def main():
    last_key = None
    for line in open('in.txt', 'r'):
        key, value = line.strip().split()
        if last_key and key != last_key:
            print(last_key)
        else:
            pass
        last_key = key

    if last_key:
        print(last_key)


if __name__ == '__main__':
    main()
