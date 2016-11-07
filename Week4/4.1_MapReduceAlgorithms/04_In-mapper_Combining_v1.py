import sys


def mapper(text):
    H = {}
    for word in text:
        if word not in H:
            H[word] = 1
        else:
            H[word] += 1

    for key in H:
        print(key, H[key], sep='\t', end='\n')


def main():
    for line in sys.stdin:
        mapper(line.strip().split(' '))


if __name__ == '__main__':
    main()
