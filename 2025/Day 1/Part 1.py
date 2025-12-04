import time

startTime = time.perf_counter()

with open("../2025/Day 1/input.txt", "r") as file:
    code = file.readlines()

zeroes = 0
dial = 50

for i in code:
    dial = (dial + (int(i[1:]) if i[0] == "R" else int(i[1:]) * -1)) % 100
    if dial == 0: zeroes += 1

print(zeroes)
print(f"Program finished in {time.perf_counter() - startTime:.4f}ms")
