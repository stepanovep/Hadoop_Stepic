import sys


def mapperWithStripe(elements):
    for i in elements:
        h = {}
        for j in elements:
            if i != j:
                if j not in h:
                    h[j] = 1
                else:
                    h[j] += 1

        print('%s\t' % i, end='')
        len = h.__len__()
        k = 0
        for key in h:
            if k < len-1:
                print('{}:{},'.format(key, h[key]), end='')
            else:
                print('{}:{}'.format(key, h[key]))
            k += 1


def main():
    for line in open('in.txt', 'r'):
        mapperWithStripe(line.strip().split())


if __name__ == '__main__':
    main()