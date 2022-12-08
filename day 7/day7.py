from collections import defaultdict
from functools import lru_cache
with open("day7.in") as file:
    sections = ("\n" + file.read().strip()).split("\n$ ")[1:]

path = []
dir_sizes = defaultdict(int)
children = defaultdict(list)

def parse(section):
    lines = section.split("\n")
    command = lines[0]
    outputs = lines[1:]
    parts = command.split(" ")
    op = parts[0]
    if op == "cd":
        if parts[1] == "..":
            path.pop()
        else:
            path.append(parts[1])
        return
    abspath = "/".join(path)
    assert op == "ls"
    sizes = []
    for line in outputs:
        if not line.startswith("dir"):
            sizes.append(int(line.split(" ")[0]))
        else:
            dir_name = line.split(" ")[1]
            children[abspath].append(f"{abspath}/{dir_name}")
    dir_sizes[abspath] = sum(sizes)

def part2():
    unused = 70000000 - search("/")
    required = 30000000 - unused

    ans = 1 << 60
    for abspath in dir_sizes:
        size = search(abspath)
        if size >= required:
            ans = min(ans, size)

    print(ans)

for block in sections:
    parse(block)

def search(absolutepath):
    size = dir_sizes[absolutepath]
    for child in children[absolutepath]:
        size += search(child)
    return size

if __name__ == "__main__":
    ans = 0
    for absolutepath in dir_sizes:
        if search(absolutepath) <= 100000:
            ans += search(absolutepath)

    print(ans)
    part2()