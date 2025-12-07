import time

startTime = time.perf_counter()

with open("../2025/Day 4/input.txt", "r") as file:
    paper = [x.strip() for x in file.readlines()]
    
totalPossible = 0

while True:
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
	for y in range(len(count)):
		for x in range(len(count[0])):
			if count[y][x] < 4:
				possible += 1
				paper[y] = paper[y][:x] + "." + paper[y][x + 1:]

	totalPossible += possible
	if possible == 0: break

print(totalPossible)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")