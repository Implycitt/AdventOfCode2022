import math
with open("day9.in", 'r') as file:
    data = file.read().split('\n')

directions = {
    'U' : [0, 1],
    'D' : [0, -1],
    'R' : [1, 0],
    'L' : [-1, 0]
}

def distance(hx, hy, tx, ty):
    dist = math.sqrt(((hx - tx)**2) + ((hy - ty)**2))
    return dist

def main():
    headx, heady = 0, 0
    tailx, taily = 0, 0
    pointspassed = set()
    for a in data:
        direction, magnitude = a.split(' ')
        magnitude = int(magnitude)
        directionaddx, directionaddy = directions[direction]
        for i in range(int(magnitude)):
            headx += directionaddx
            heady += directionaddy
            if distance(headx, heady, tailx, taily) >= 2:
                signx = 0 if headx == tailx else (headx - tailx) / abs(headx - tailx)
                signy = 0 if heady == taily else (heady - taily) / abs(heady - taily)
                tailx += signx
                taily += signy
            pointspassed.add((tailx, taily))
            
    print(len(pointspassed))

def mainpart2():
    knots = []
    for i in range(10):
        knots.append([0, 0])
    pointspassed = set()
    for a in data:
        direction, magnitude = a.split(' ')
        magnitude = int(magnitude)
        directionaddx, directionaddy = directions[direction]
        for i in range(int(magnitude)):
            knots[0][0] += directionaddx
            knots[0][1] += directionaddy
            for j in range(1, 10):
                headx, heady = knots[j - 1]
                tailx, taily = knots[j]
                if distance(headx, heady, tailx, taily) >= 2:
                    signx = 0 if headx == tailx else (headx - tailx) / abs(headx - tailx)
                    signy = 0 if heady == taily else (heady - taily) / abs(heady - taily)
                    tailx += signx
                    taily += signy
                knots[j] = [tailx, taily]
            pointspassed.add(tuple(knots[-1]))
                
    print(len(pointspassed))

if __name__ == "__main__":
    main()
    mainpart2()