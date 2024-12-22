import numpy as np


input_str = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()

with open("input_day10.txt", "r") as f:
    input_str = f.read().strip()

topo_map = np.array([[int(height) for height in row] for row in input_str.split("\n")])

trailhead_map = np.zeros_like(topo_map)
h, w = topo_map.shape


def find_peaks(x: int, y: int):
    if topo_map[y, x] == 9:
        return set([(x, y)])

    reachable_peaks = set()

    if 0 <= x - 1 < w and topo_map[y, x - 1] == topo_map[y, x] + 1:
        reachable_peaks |= find_peaks(x=x - 1, y=y)
    if 0 <= x + 1 < w and topo_map[y, x + 1] == topo_map[y, x] + 1:
        reachable_peaks |= find_peaks(x=x + 1, y=y)
    if 0 <= y - 1 < h and topo_map[y - 1, x] == topo_map[y, x] + 1:
        reachable_peaks |= find_peaks(x=x, y=y - 1)
    if 0 <= y + 1 < h and topo_map[y + 1, x] == topo_map[y, x] + 1:
        reachable_peaks |= find_peaks(x=x, y=y + 1)

    return reachable_peaks


total_score = 0

for i in range(len(topo_map)):
    for j in range(len(topo_map[i])):
        if topo_map[i, j] == 0:
            peaks = find_peaks(x=j, y=i)
            score = len(peaks)
            total_score += score

print(total_score)


def find_trails(x: int, y: int):
    if topo_map[y, x] == 9:
        return 1

    complete_trails = 0

    if 0 <= x - 1 < w and topo_map[y, x - 1] == topo_map[y, x] + 1:
        complete_trails += find_trails(x=x - 1, y=y)
    if 0 <= x + 1 < w and topo_map[y, x + 1] == topo_map[y, x] + 1:
        complete_trails += find_trails(x=x + 1, y=y)
    if 0 <= y - 1 < h and topo_map[y - 1, x] == topo_map[y, x] + 1:
        complete_trails += find_trails(x=x, y=y - 1)
    if 0 <= y + 1 < h and topo_map[y + 1, x] == topo_map[y, x] + 1:
        complete_trails += find_trails(x=x, y=y + 1)

    return complete_trails


total_rating = 0

for i in range(len(topo_map)):
    for j in range(len(topo_map[i])):
        if topo_map[i, j] == 0:
            rating = find_trails(x=j, y=i)
            total_rating += rating

print(total_rating)
