from functools import cmp_to_key 

def convert(list):
    returning = [list]
    return returning

def main(a, b):
    if type(a) == int and type(b) == list:
        a = convert(a)
    if type(b) == int and type(a) == list:
        b = convert(b)

    if type(a) == int and type(b) == int:
        if a < b:
            return 1
        if a == b:
            return 0
        return -1
    
    if type(a) == list and type(b) == list:
        i = 0
        while i < len(a) and i < len(b):
            x = main(a[i], b[i]) # recursion !!!!
            if x == 1:
                return 1
            if x == -1:
                return -1
            i += 1

        if i == len(a):
            if len(a) == len(b):
                return 0
            return 1
        return -1

def part2(arr):
    sortedLists = list(map(eval, arr))
    sortedLists.append([[2]])
    sortedLists.append([[6]])
    sortedLists = sorted(sortedLists, key=cmp_to_key(main), reverse=True)

    for i, instance in enumerate(sortedLists):
        if instance == [[2]]:
            a = i + 1
        if instance == [[6]]:
            b = i + 1
    print(a * b)


if __name__ == "__main__":
    with open("day13.in", 'r') as file:
        data = file.read().split('\n\n')
    answer = 0
    for i, part in enumerate(data):
        firstpart, secondpart = map(eval, part.split("\n"))
        if main(firstpart, secondpart) == 1:
            answer += i + 1
    print(answer)
    with open("day13.in", 'r') as file:
        data = file.read().strip().replace("\n\n", "\n").split("\n")
    part2(data)