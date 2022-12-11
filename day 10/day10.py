with open("day10.in", 'r') as file:
    data = file.read().split('\n')

def part1():
    ticks = 0
    registerx = 1
    totalstrength = 0

    for i in data:

        if i != "noop":
            command, magnitude = i.split(' ')
            magnitude = int(magnitude)
            registerx += magnitude
            ticks += 1
            if ticks == 20 or ticks == 60 or ticks == 100 or ticks == 140 or ticks == 180 or ticks == 220:
                totalstrength += ticks*(registerx-magnitude)
            ticks += 1
            if ticks == 20 or ticks == 60 or ticks == 100 or ticks == 140 or ticks == 180 or ticks == 220:
                totalstrength += ticks*(registerx-magnitude)

        elif i == "noop":
            ticks += 1
            if ticks == 20 or ticks == 60 or ticks == 100 or ticks == 140 or ticks == 180 or ticks == 220:
                totalstrength += ticks*registerx
    print(totalstrength)

def part2():

    ticks = 0
    registerx = 1
    totalstrength = 0
    row = 0
    column = 0
    horizontalposition = [1] * 241
    for i in data:

        if i != "noop":
            command, magnitude = i.split(' ')
            magnitude = int(magnitude)
            horizontalposition[ticks + 1] = registerx
            registerx += magnitude
            ticks += 2
            horizontalposition[ticks] = registerx

        elif i == "noop":
            ticks += 1
            horizontalposition[ticks] = registerx
    
    totalstrength = [[None] * 40 for i in range(6)]
    for row in range(6):
        for column in range(40):
            counter = row  * 40 + column + 1
            if abs(horizontalposition[counter - 1] - (column)) <= 1:
                totalstrength[row][column] = "##"
            else:
                totalstrength[row][column] = "  "

    for row in totalstrength:
        print("".join(row))


if __name__ == "__main__":
    # part1()
    part2()
