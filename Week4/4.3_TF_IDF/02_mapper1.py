import sys
import re


def mapper(num, text):
    text = re.split(r'[\W]+', text)
    for word in text:
        if word.__len__() > 0:
            print('{}#{}\t{}'.format(word, num, 1))


def main():
    for line in open('in.txt', 'r'):
        num, text = line.strip().split(':', 1)
        mapper(num, text)


if __name__ == '__main__':
    main()