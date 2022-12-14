with open("day11.in", 'r') as file:
    data = file.read().split('\n\n')

class Monkey:
    def __init__(self, *startingitems, operation, test, inspects):
        self.startingitems = startingitems
        self.operation = operation
        self.test = test
        self.inspects = inspects

if __name__ == "__main__":
    print(data)