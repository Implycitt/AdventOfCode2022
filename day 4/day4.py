import re
with open("day4.in", 'r') as file:
    data = file.read().split('\n')

def elfAreas(arr):
    areas = []
    for i in data:
        areas.append(re.split(r'[,-]', i))
    
    assignmentpairs = 0
    for i in areas:
        firstguyarea = []
        secondguyarea = []
        for k in range(int(i[0]), int(i[1])+1):
            firstguyarea.append(k) 
        for j in range(int(i[2]), int(i[3])+1):
            secondguyarea.append(j)
        trueifall = True
        if len(firstguyarea) < len(secondguyarea):
            for u in firstguyarea:
                if u not in secondguyarea:
                    trueifall = False
                    break
            if trueifall:
                assignmentpairs += 1
        else:
            for u in secondguyarea:
                if u not in firstguyarea:
                    trueifall = False
                    break
            if trueifall:
                assignmentpairs += 1
    print(assignmentpairs)

def overlapatall(arr):
    areas = []
    for i in data:
        areas.append(re.split(r'[,-]', i))

    pairs = 0
    for i in areas:
        firstguyarea = []
        secondguyarea = []
        for k in range(int(i[0]), int(i[1])+1):
            firstguyarea.append(k) 
        for j in range(int(i[2]), int(i[3])+1):
            secondguyarea.append(j)

        if len(firstguyarea) < len(secondguyarea):
            for u in firstguyarea:
                if u in secondguyarea:
                    pairs += 1
                    break
        else:
            for u in secondguyarea:
                if u in firstguyarea:
                    pairs += 1
                    break
    print(pairs)

def main():
    # elfAreas(data)
    overlapatall(data)

if __name__ == "__main__":
    print(main())