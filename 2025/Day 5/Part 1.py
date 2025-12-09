import time

startTime = time.perf_counter()

with open("../2025/Day 5/input.txt", "r") as file:
	freshIDs = [x.strip() for x in file.readlines()]
	
idRanges = []

for i, x in enumerate(freshIDs):
	if x == "": break
	idRanges.append([int(j) for j in x.split("-")])

ids = [int(x) for x in freshIDs[i + 1:]]
fresh = 0

for x in ids:
	for j in idRanges:
		if x >= j[0] and x <= j[1]:
			fresh += 1
			break

print(fresh)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")