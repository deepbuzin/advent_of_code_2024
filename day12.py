from queue import Queue
from typing import Tuple
import numpy as np

input_str = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip()

with open("input_day12.txt", "r") as f:
    input_str = f.read().strip()

garden = [[plant for plant in row] for row in input_str.split("\n")]

h, w = len(garden), len(garden[0])
mask = np.zeros((h, w), dtype=bool)


def find_plot(plant: str, q: Queue[Tuple[int, int]]) -> int:
    perimeter = 0
    area = 0
    sides = 0

    side_masks = {
        "up": np.zeros((h + 2, w + 2), dtype=bool),
        "down": np.zeros((h + 2, w + 2), dtype=bool),
        "left": np.zeros((h + 2, w + 2), dtype=bool),
        "right": np.zeros((h + 2, w + 2), dtype=bool),
    }

    def mark_side_mask(direction, i, j):
        side_masks[direction][i + 1, j + 1] = True

    while not q.empty():
        i, j = q.get()
        mask[i, j] = True
        area += 1

        if 0 <= i - 1 < h and garden[i - 1][j] == plant:
            if not mask[i - 1, j] and (i - 1, j) not in q.queue:
                q.put((i - 1, j))
        else:
            perimeter += 1
            mark_side_mask("up" , i - 1, j)

            # is new horizontal side in up direction
            if not side_masks["up"][i - 1 + 1, j + 1 - 1] and not side_masks["up"][i - 1 + 1, j + 1 + 1]:
                sides += 1


        if 0 <= i + 1 < h and garden[i + 1][j] == plant:
            if not mask[i + 1, j] and (i + 1, j) not in q.queue:
                q.put((i + 1, j))
        else:
            perimeter += 1
            mark_side_mask("down" , i + 1, j)

            # is new horizontal side in up direction
            if not side_masks["down"][i + 1 + 1, j + 1 - 1] and not side_masks["down"][i + 1 + 1, j + 1 + 1]:
                sides += 1


        if 0 <= j - 1 < w and garden[i][j - 1] == plant:
            if not mask[i, j - 1] and (i, j - 1) not in q.queue:
                q.put((i, j - 1))
        else:
            perimeter += 1
            mark_side_mask("left" , i, j - 1)

            # is new horizontal side in up direction
            if not side_masks["left"][i + 1 - 1, j - 1 + 1] and not side_masks["left"][i + 1 + 1, j - 1 + 1]:
                sides += 1


        if 0 <= j + 1 < w and garden[i][j + 1] == plant:
            if not mask[i, j + 1] and (i, j + 1) not in q.queue:
                q.put((i, j + 1))
        else:
            perimeter += 1
            mark_side_mask("right" , i, j + 1)

            # is new horizontal side in up direction
            if not side_masks["right"][i + 1 - 1, j + 1 + 1] and not side_masks["right"][i + 1 + 1, j + 1 + 1]:
                sides += 1

    return area, perimeter, sides


total_price = 0
total_bulk_price = 0

for i in range(h):
    for j in range(w):
        if not mask[i, j]:
            q = Queue()
            q.put((i, j))
            area, perimeter, sides = find_plot(plant=garden[i][j], q=q)
            price = area * perimeter
            bulk_price = area * sides
            # print(f"{garden[i][j]}, {area}, {perimeter}, {price}")
            # print(mask)
            print(sides)
            total_price += price
            total_bulk_price += bulk_price


print(total_price)
print(total_bulk_price)
