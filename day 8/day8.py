import numpy
with open("day8.in", 'r') as file:
    data = file.read().split('\n')

createGrid = [list(map(int, list(line))) for line in data]
row = len(createGrid)
column = len(createGrid[0])
createGrid = numpy.array(createGrid)

def insideCheck():
    visible = 0
    score = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    answer = 0
    for i in range(row):
        for j in range(column):
            currentTree = createGrid[i, j]
            if j == 0 or numpy.amax(createGrid[i, :j]) < currentTree:
                visible += 1
            elif j == column - 1 or numpy.amax(createGrid[i, (j + 1):]) < currentTree:
                visible += 1
            elif i == 0 or numpy.amax(createGrid[:i, j]) < currentTree:
                visible += 1
            elif i == row - 1 or numpy.amax(createGrid[(i + 1):, j]) < currentTree:
                visible += 1

    print(visible)


def scoreChecker():
    dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    answer = 0
    for i in range(row):
        for j in range(column):
            currentTree = createGrid[i, j]
            score = 1
            for di, dj in dd:
                ii, jj = i + di, j + dj
                distance = 0
                while (0 <= ii < row and 0 <= jj < column) and createGrid[ii, jj] < currentTree:
                    distance += 1
                    ii += di
                    jj += dj
                    if (0 <= ii < row and 0 <= jj < column) and createGrid[ii, jj] >= currentTree:
                        distance += 1
                score *= distance
                
            answer = max(answer, score)

    print(answer)

if __name__ == "__main__":
    # insideCheck()
    scoreChecker()