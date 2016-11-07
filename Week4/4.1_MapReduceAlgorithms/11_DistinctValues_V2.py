import sys



class ReducerV2:
    def __init__(self):
        self.H = {}

    def reduce(self, f, categories):
        categories = list(set(categories))
        for category in categories:
            if category not in self.H:
                self.H[category] = 1
            else:
                self.H[category] += 1



def main():
    reducer = ReducerV2()

    last_f = None
    categories = []
    for line in open('in.txt', 'r'):
        f, category = line.strip().split()
        if last_f and last_f != f:
            reducer.reduce(last_f, categories)
            categories = [category]
        else:
            categories += [category]

        last_f = f

    if last_f:
        reducer.reduce(f, categories)

    for category in reducer.H:
        print(category, reducer.H[category], sep='\t')


if __name__ == '__main__':
    main()
