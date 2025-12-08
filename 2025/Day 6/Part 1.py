import time

startTime = time.perf_counter()

with open("../2025/Day 6/input.txt", "r") as file:
    unorderedNums = [[i for i in x.strip().split(" ") if i] for x in file.readlines()]

nums = []
for i in range(len(unorderedNums[0])):
    nums.append([])
    for j in range(len(unorderedNums)):
        nums[i].append(unorderedNums[j][i])

totalSum = 0

for x in nums:
    if x[-1] == "+": totalSum += sum([int(x) for x in x[:-1]])
    else:
        product = 1
        for j in x[:-1]: product *= int(j)
        totalSum += product

print(totalSum)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")
