import time

startTime = time.perf_counter()

with open("../2025/Day 3/input.txt", "r") as file:
    voltages = file.readlines()

volts = 0

for i in voltages:
    maxVolts = [0, 0]
    for j, v in enumerate(i[:-2]):
        if int(v) > maxVolts[0]: maxVolts = [int(v), j]

    volts += int(str(maxVolts[0]) + str(max(i[maxVolts[1] + 1:])))

print(volts)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")
