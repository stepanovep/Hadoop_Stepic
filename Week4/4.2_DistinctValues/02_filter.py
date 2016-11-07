import sys


def main():
    the_id = 'user10'

    for line in sys.stdin:
        time, id, url = line.strip().split()
        if id == the_id:
            print('{}\t{}\t{}'.format(time, id, url))


if __name__ == '__main__':
    main()