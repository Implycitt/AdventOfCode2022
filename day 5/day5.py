import re
with open("day5.in", 'r') as file:
    data = file.read().split('\n')

filteredData = []
for i in data:
    if i[0] == 'm':
        filteredData.append(re.split(r'[move from to]', i))

ocolumns = [
    ['F', 'G', 'V', 'R', 'J', 'L', 'D'],
    ['S', 'J', 'H', 'V', 'B', 'M', 'P', 'T'],
    ['C', 'P', 'G', 'D', 'F', 'M', 'H', 'V'],
    ['Q', 'G', 'N', 'P', 'D', 'M'],
    ['F', 'N', 'H', 'L', 'J'],
    ['Z', 'T', 'G', 'D', 'Q', 'V', 'F', 'N'],
    ['L', 'B', 'D', 'F'],
    ['N', 'D', 'V', 'S', 'B', 'J', 'M'],
    ['D', 'L', 'G']
]
numbermoving = []
columnfrom = []
columnto = []
answer = []
ncolumns = []

for i in ocolumns:
    ncolumns.append(i[::-1])

def moveboxes():
    for i in filteredData:
        numbermoving = int(i[5])
        columnfrom = int((i[11])) -1
        columnto = int((i[15])) - 1

        for j in range(numbermoving):
            remove = ncolumns[columnfrom].pop()
            ncolumns[columnto].append(remove)

    for i in ncolumns:
        answer.append(i[-1])
    print(''.join(answer))

def part2moveboxes():
    for i in filteredData:
        numbermoving = int(i[5])
        columnfrom = int((i[11])) -1
        columnto = int((i[15])) - 1

        ncolumns[columnto].extend(ncolumns[columnfrom][-numbermoving:])
        ncolumns[columnfrom] = ncolumns[columnfrom][:-numbermoving]

    for i in ncolumns:
        answer.append(i[-1])
    print(''.join(answer))

def main():
    # moveboxes()
    part2moveboxes()

if __name__ == "__main__":
    main()