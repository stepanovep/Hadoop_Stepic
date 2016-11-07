import sys


def mapperV2(text):
    H = {}
    for line in text:
        for word in line.strip().split(' '):
            if word not in H:
                H[word] = 1
            else:
                H[word] += 1

    for key in H:
        print(key, H[key], sep='\t', end='\n')


def main():
    mapperV2(sys.stdin)


if __name__ == '__main__':
    main()
