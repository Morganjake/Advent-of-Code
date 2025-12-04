import time

startTime = time.perf_counter()

with open("../2025/Day 2/input.txt", "r") as file:
    Ids = [x.split("-") for x in file.readline().split(",")]

invalidSum = 0

for id1, id2 in Ids:
    invalidIDHalf = int(id1[:len(id1) // 2]) if len(id1) % 2 == 0 else 10 ** (len(id1) // 2)
    invalidID = int(str(invalidIDHalf) * 2)

    while invalidID <= int(id2):
        if invalidID >= int(id1):
            invalidSum += invalidID
        invalidIDHalf += 1
        invalidID = int(str(invalidIDHalf) * 2)

print(invalidSum)
print(f"Program finished in {time.perf_counter() - startTime:.4f}ms")
