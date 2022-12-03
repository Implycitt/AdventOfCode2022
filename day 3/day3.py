with open("day3.in", 'r') as file:
    data = file.read().split('\n')

firstCompartment, secondCompartment = [i[:len(i)//2] for i in data], [i[len(i)//2:] for i in data]

def checkCommon(arr, secarr):
    commonCharacters = []
    for i in range(len(arr)):
        tof = False
        for j in arr[i]:
            if tof == True:
                break
            for k in secarr[i]:
                if j == k:
                    commonCharacters.append(j) 
                    tof = True
                    break
    return commonCharacters 

def checkCommonP2(arr, secarr, tarr):
    commonCharacters = []
    found = False
    for i in range(len(min(arr, secarr, tarr, key=len))):
        for i in arr:
            if found:
                break
            for j in secarr:
                if found:
                    break
                for k in tarr:
                    if i == j and j == k:
                        # print(i, j, k)
                        commonCharacters.append(i)
                        found = True
                        break
    return commonCharacters

def priorities(string):
    priority = 0
    if string.islower() == True:
        priority = int(ord(string))-96
    else:
        priority = int(ord(string))-64+26
    return priority

def main():
    sumofpriorities = 0
    characters = checkCommon(list(firstCompartment), list(secondCompartment))
    for i in characters:
        sumofpriorities += int(priorities(i))
    return sumofpriorities

def main2(arr):
    sumofpriorities = 0
    characters = []
    for i in range(0, len(arr)-2, 3):
        characters.append(''.join(str(e) for e in checkCommonP2(arr[i], arr[i+1], arr[i+2])))
    for i in characters:
        sumofpriorities += int(priorities(i))
    return sumofpriorities

if __name__ == "__main__":
    # print(main())
    print(main2(data))