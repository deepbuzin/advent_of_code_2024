from queue import Queue
from typing import Tuple
import numpy as np


with open("input_day12.txt", "r") as f:
    input_str = f.read().strip()

garden = [[plant for plant in row] for row in input_str.split("\n")]

h, w = len(garden), len(garden[0])
mask = np.zeros((h, w), dtype=bool)


def find_plot(plant: str, q: Queue[Tuple[int, int]]) -> int:
    perimeter = 0
    area = 0

    plot_mask = np.zeros_like(mask, dtype=bool)

    while not q.empty():
        i, j = q.get()
        mask[i, j] = True
        plot_mask[i, j] = True
        area += 1

        for _i, _j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= _i < h and 0 <= _j < w and garden[_i][_j] == plant:
                if not mask[_i, _j] and (_i, _j) not in q.queue:
                    q.put((_i, _j))
            else:
                perimeter += 1

    # find corners
    corner_mask = np.zeros_like(plot_mask, dtype=int)

    for i in range(h):
        for j in range(w):
            # is outer upper left
            if (
                plot_mask[i, j]
                and not (0 <= j - 1 < w and plot_mask[i, j - 1])
                and not (0 <= i - 1 < h and plot_mask[i - 1, j])
            ):
                corner_mask[i, j] += 1
            # is outer upper right
            if (
                plot_mask[i, j]
                and not (0 <= j + 1 < w and plot_mask[i, j + 1])
                and not (0 <= i - 1 < h and plot_mask[i - 1, j])
            ):
                corner_mask[i, j] += 1
            # is outer lower left
            if (
                plot_mask[i, j]
                and not (0 <= j - 1 < w and plot_mask[i, j - 1])
                and not (0 <= i + 1 < h and plot_mask[i + 1, j])
            ):
                corner_mask[i, j] += 1
            # is outer lower right
            if (
                plot_mask[i, j]
                and not (0 <= j + 1 < w and plot_mask[i, j + 1])
                and not (0 <= i + 1 < h and plot_mask[i + 1, j])
            ):
                corner_mask[i, j] += 1

            # is inner upper left
            if (
                plot_mask[i, j]
                and (0 <= j - 1 < w and plot_mask[i, j - 1])
                and (0 <= i - 1 < h and plot_mask[i - 1, j])
                and not (0 <= i - 1 < h and 0 <= j - 1 < w and plot_mask[i - 1, j - 1])
            ):
                corner_mask[i, j] += 1
            # is inner upper right
            if (
                plot_mask[i, j]
                and (0 <= j + 1 < w and plot_mask[i, j + 1])
                and (0 <= i - 1 < h and plot_mask[i - 1, j])
                and not (0 <= i - 1 < h and 0 <= j + 1 < w and plot_mask[i - 1, j + 1])
            ):
                corner_mask[i, j] += 1
            # is inner lower left
            if (
                plot_mask[i, j]
                and (0 <= j - 1 < w and plot_mask[i, j - 1])
                and (0 <= i + 1 < h and plot_mask[i + 1, j])
                and not (0 <= i + 1 < h and 0 <= j - 1 < w and plot_mask[i + 1, j - 1])
            ):
                corner_mask[i, j] += 1
            # is inner lower right
            if (
                plot_mask[i, j]
                and (0 <= j + 1 < w and plot_mask[i, j + 1])
                and (0 <= i + 1 < h and plot_mask[i + 1, j])
                and not (0 <= i + 1 < h and 0 <= j + 1 < w and plot_mask[i + 1, j + 1])
            ):
                corner_mask[i, j] += 1

    sides = np.sum(corner_mask)
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
            total_price += price
            total_bulk_price += bulk_price

print(total_price)
print(total_bulk_price)
