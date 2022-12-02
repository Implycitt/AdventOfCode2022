with open("day2.in", 'r') as file:
    data = file.read().split('\n')

def check(arr):
    response = {'X': 1, 'Y': 2, 'Z': 3}
    wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    translate = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    total = 0
    for i in arr:
        play = i[0]
        answer = i[2]
        if wins[play] == i[2]:
            total += 6
        elif play == translate[answer]:
            total += 3
        total += int(response[answer])

    return total

def whatToPlay(arr):
    total = 0
    condition = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
    wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    losing = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    points = {'X': 1, 'Y': 2, 'Z': 3}
    response = {'X': 0, 'Y': 3, 'Z': 6}
    for i in arr:
        WLorD = i[2]
        play = i[0]
        whattodo = condition[WLorD]
        if whattodo == "Lose":
            total += points[losing[play]]
        elif whattodo == "Draw":
            total += points[draw[play]]
        else:
            total += points[wins[play]]
        total += response[WLorD]
        
    return total             

def main():
    # return check(data)
    return whatToPlay(data)

if __name__ == "__main__":
    print(main())    