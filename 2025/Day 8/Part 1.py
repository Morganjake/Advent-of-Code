import time

startTime = time.perf_counter()

with open("../2025/Day 8/input.txt", "r") as file:
    junctions = [[int(j) for j in x.split(",")] for x in file.readlines()]


edges = []
for i, j in enumerate(junctions[:-1]):
    for k in junctions[i + 1:]:
        x, y, z = j[0] - k[0], j[1] - k[1], j[2] - k[2]
        hyp = (x * x + y * y + z * z) ** 0.5
        edges.append([hyp, j, k])

sortedEdges = sorted(edges)
clusters = {tuple(x): [x] for x in junctions}

for i in range(1000):
    edge = sortedEdges[i]
    if edge[2] in clusters[tuple(edge[1])]: continue

    for x in clusters[tuple(edge[2])]:
        clusters[tuple(edge[1])].append(x)

    for x in clusters[tuple(edge[2])]:
        clusters[tuple(x)] = clusters[tuple(edge[1])]

allClusters = []
for x in clusters:
    for j in allClusters:
        if clusters[x] == j: break
    else: allClusters.append(clusters[x])

sortedClusterSizes = sorted([len(x) for x in allClusters], reverse=True)
mult = 1
for x in sortedClusterSizes[:3]: mult *= x

print(mult)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")
