import time

startTime = time.perf_counter()

with open("../2025/Day 2/input.txt", "r") as file:
    Ids = [x.split("-") for x in file.readline().split(",")]

invalidSum = 0

for id1, id2 in Ids:
    
    split = 2
    prevSplits = set()

    while split <= len(id2):
        if len(id1) % split == 0: invalidIDHalf = int(id1[:len(id1) // split])
        else: invalidIDHalf = 10 ** (len(id1) // split)
        invalidID = int(str(invalidIDHalf) * split)

        while invalidID <= int(id2):
            if invalidID >= int(id1) and invalidID not in prevSplits:
                prevSplits.add(invalidID)
                invalidSum += invalidID

            invalidIDHalf += 1
            invalidID = int(str(invalidIDHalf) * split)

        split += 1

print(invalidSum)
print(f"Program finished in {time.perf_counter() - startTime:.4f}ms")
