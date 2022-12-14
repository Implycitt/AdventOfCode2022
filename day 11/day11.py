monkeys = []

for group in open("day11.in", 'r').read().strip().split("\n\n"):
    data = group.splitlines()
    monkey = []
    monkey.append(list(map(int, data[1].split(": ")[1].split(", "))))
    monkey.append(eval("lambda old:" + data[2].split('=')[1]))
    for part in data[3:]:
        monkey.append(int(part.split()[-1]))
    monkeys.append(monkey)


def simulate1():
    count = [0] * len(monkeys)
    for i in range(20):
        for index, monkey, in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item //= 3
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            count[index] += len(monkey[0])
            monkey[0] = []
    return count

def simulate2():
    count = [0] * len(monkeys)
    mod = 1
    for monkey in monkeys:
            mod *= monkey[2]

    for i in range(10000):
        for index, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item %= mod
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            count[index] += len(monkey[0])
            monkey[0] = []
    return count


if __name__ == "__main__":
    count = simulate1()
    count.sort()
    print(count[-1] * count[-2])
    count = simulate2()
    count.sort()
    print(count[-1] * count[-2])