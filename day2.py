import numpy as np


levels = []

with open("input_day2.txt", "r") as f:
    for line in f.readlines():
        levels.append(np.array([int(num) for num in line.split(" ")]))

safe_count = 0
dampened_safe_count = 0


def check_level(level):
    diff = np.diff(level)

    mono = np.logical_or(np.cumsum(diff < 0) == 0, np.cumsum(diff > 0) == 0)
    spiking = np.logical_not(np.logical_and(np.abs(diff) >= 1, np.abs(diff) <= 3))

    safe = np.logical_and(mono, np.logical_not(spiking))
    return safe


for level in levels:
    safe = np.all(check_level(level))
    dampened_safe = np.any(
        [np.all(check_level(np.delete(level, i))) for i in range(len(level))]
    )

    if safe:
        safe_count += 1
        dampened_safe_count += 1
    elif dampened_safe:
        dampened_safe_count += 1

print(safe_count)
print(dampened_safe_count)
