import time

startTime = time.perf_counter()

with open("../2025/Day 3/input.txt", "r") as file:
    voltages = [x.strip() + "_" for x in file.readlines()]

volts = 0

for i in voltages:

    first = 0
    voltage = ""
    for j in range(12):

        maxVolts = [0, 0]
        for k, x in enumerate(i[first:-(12-j)]):
            if int(x) > maxVolts[0]: maxVolts = [int(x), k]
            if x == "9": break

        first += maxVolts[1] + 1
        voltage += str(maxVolts[0])

    volts += int(voltage)

print(volts)
print(f"Program finished in {time.perf_counter() - startTime:.4f} seconds")
