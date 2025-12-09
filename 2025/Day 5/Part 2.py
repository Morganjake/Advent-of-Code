import time

startTime = time.perf_counter()

with open("../2025/Day 5/input.txt", "r") as file:
	freshIDs = [x.strip() for x in file.readlines()]
	
idRanges = []

for i, x in enumerate(freshIDs):
	if x == "": break
	idRange = [int(j) for j in x.split("-")]
	
	j = 0
	add = True
	while j < len(idRanges) and add:
		k = idRanges[j]
		if idRange[0] >= k[0] and idRange[1] <= k[1]:
			add = False
		elif idRange[0] <= k[0] and idRange[1] >= k[1]:
			del idRanges[j]
		elif idRange[0] >= k[0] and idRange[0] <= k[1]:
			idRange[0] = k[0]
			del idRanges[j]
		elif idRange[1] >= k[0] and idRange[1] <= k[1]:
			idRange[1] = k[1]
			del idRanges[j]
		else: j += 1

	if add: idRanges.append(idRange)

freshIDCount = 0

for x in idRanges:
	freshIDCount += x[1] - x[0] + 1

print(freshIDCount)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")