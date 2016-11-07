import sys


def main():

    [lastkey, cursum, curcnt] = [None, 0, 0]

    for line in sys.stdin:
        [key, values] = line.strip().split()
        [value, cnt] = map(int, values.split(';')
        )
        if lastkey and key != lastkey:
            print(lastkey + '\t' + str(cursum)+';'+str(curcnt), end='\n')
            cursum = value
            curcnt = 1
        else:
            cursum += value
            curcnt += 1

        lastkey = key

    if lastkey:
        print(lastkey + '\t' + str(cursum)+';'+str(curcnt), end='\n')

if __name__ == '__main__':
    main()


