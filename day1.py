with open("day1.in", 'r') as file:
    data = file.read().split('\n')

maxCalories = []

def suming(arr):
    sums = 0
    for i in arr:
        if i == '':
            maxCalories.append(sums)
            sums = 0
            continue
        sums = sums + int(i)
    return maxCalories

top3elves = suming(data)
top3elves.sort(reverse=1)

print(top3elves[0]+top3elves[1]+top3elves[2])
print(max(suming(data)))