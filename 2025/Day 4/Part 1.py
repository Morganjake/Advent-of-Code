import time

startTime = time.perf_counter()

with open("../2025/Day 4/input.txt", "r") as file:
    paper = [x.strip() for x in file.readlines()]

count = [[0 for _ in range(len(paper[0]))] for _ in range(len(paper))]
offsets = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

for y in range(len(paper)):
    for x in range(len(paper[0])):
        if paper[y][x] == "@":
            for offset in offsets:
                if y + offset[0] >= 0 and y + offset[0] < len(paper):
                    if x + offset[1] >= 0 and x + offset[1] < len(paper[0]):
                        count[y + offset[0]][x + offset[1]] += 1
        else: count[y][x] += 100

possible = 0

for x in count:
    for i in x:
        if i < 4: possible += 1

print(possible)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")