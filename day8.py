import re
from collections import defaultdict


with open("input_day8.txt", "r") as f:
    input_str = f.read().strip()

pattern = r"([0-9A-Za-z])"
lines = input_str.split("\n")
h, w = len(lines), len(lines[0])


antennas = defaultdict(list)

for match in re.finditer(pattern, input_str, re.M):
    idx = match.start(0)
    antennas[match.group(0)].append((idx // (w + 1), idx % (w + 1)))

antinodes = set()

for freq, locations in antennas.items():
    for i, (x1, y1) in enumerate(locations):
        for j, (x2, y2) in enumerate(locations[i + 1 :]):
            x_diff, y_diff = x2 - x1, y2 - y1
            an1 = x1 - x_diff, y1 - y_diff
            an2 = x2 + x_diff, y2 + y_diff

            for x_an, y_an in [an1, an2]:
                if 0 <= x_an < h and 0 <= y_an < w:
                    antinodes.add((x_an, y_an))

print(len(list(antinodes)))

resonant_antinodes = set()

for freq, locations in antennas.items():
    for i, (x1, y1) in enumerate(locations):
        for j, (x2, y2) in enumerate(locations[i + 1 :]):
            x_diff, y_diff = x2 - x1, y2 - y1

            t_range = max(h // x_diff, w // y_diff)
            ans = [
                (x2 + (t * x_diff), y2 + (t * y_diff)) for t in range(-t_range, t_range)
            ]

            for x_an, y_an in ans:
                if 0 <= x_an < h and 0 <= y_an < w:
                    resonant_antinodes.add((x_an, y_an))

print(len(list(resonant_antinodes)))
