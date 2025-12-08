import time

startTime = time.perf_counter()

with open("../2025/Day 6/input.txt", "r") as file:
    nums = [x.rstrip() for x in file.readlines()]

totalSum = 0

operators = [x for x in nums[-1].split(" ") if x]
curNums = ["" for x in range(len(nums) - 1)]

while True:
    allSpaces = True
    done = True
    for i in range(len(nums) - 1):
        if not nums[i]:
            curNums[i] += "_"
            continue
        done = False
        if nums[i][0] == " ": curNums[i] += "_"
        else:
            curNums[i] += nums[i][0]
            allSpaces = False
        nums[i] = nums[i][1:]

    if allSpaces or done:
        newNums = []
        for i in range(len(curNums[0])):
            newNums.append("")
            for j in range(len(curNums)):
                if curNums[j][i] != "_": newNums[i] += curNums[j][i]

        curNums = ["" for x in range(len(nums) - 1)]

        if operators[0] == "+":
            totalSum += sum([int(x) for x in newNums[:-1]])
        else:
            product = 1
            for x in newNums[:-1]: product *= int(x)
            totalSum += product
        operators = operators[1:]

    if done: break

print(totalSum)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")