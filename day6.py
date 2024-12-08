import numpy as np
from copy import deepcopy


with open("input_day6.txt", "r") as f:
    input_str = f.read().strip()

initial_pos = []
lab_map = []

for i, row in enumerate(input_str.split("\n")):
    lab_map.append([symbol for symbol in row])
    if row.find("^") > -1:
        current_pos = [i, row.find("^")]


def vec_to_coef(direction: np.ndarray) -> int:
    if all(direction == np.array([-1, 0])):
        return 0  # up
    elif all(direction == np.array([0, 1])):
        return 1  # right
    elif all(direction == np.array([1, 0])):
        return 2  # down
    elif all(direction == np.array([0, -1])):
        return 3  # left


def rotate_direction(direction: np.ndarray):
    return np.dot(direction, np.array([[0, -1], [1, 0]]))


def traverse_map(lab_map, guard_map, current_pos, current_dir):
    h, w, _ = guard_map.shape

    while True:
        guard_map[*current_pos, vec_to_coef(current_dir)] += 1
        future_pos = current_pos + current_dir

        if not (0 <= future_pos[0] < h and 0 <= future_pos[1] < w):
            # out of bounds
            break

        if lab_map[future_pos[0]][future_pos[1]] == "#":
            # obstacle
            current_dir = rotate_direction(current_dir)
            continue

        if guard_map[*current_pos, vec_to_coef(current_dir)] > 1:
            # closed the loop
            break

        # make a step
        current_pos = future_pos

    return guard_map, current_pos, current_dir


initial_pos = np.array(current_pos)
initial_dir = np.array([-1, 0])

guard_map, last_pos, last_dir = traverse_map(
    lab_map,
    guard_map=np.zeros((len(lab_map), len(lab_map[0]), 4), dtype=int),
    current_pos=initial_pos,
    current_dir=initial_dir,
)

num_visited = (guard_map.sum(axis=2) > 0).astype(np.uint8).sum()
print(num_visited)

count_loops = 0

for i in range(len(lab_map)):
    for j in range(len(lab_map[0])):
        if any(guard_map[i, j, :] == 1):
            new_lab_map = deepcopy(lab_map)
            new_lab_map[i][j] = "#"

            new_guard_map, last_pos, last_dir = traverse_map(
                new_lab_map,
                guard_map=np.zeros((len(lab_map), len(lab_map[0]), 4), dtype=int),
                current_pos=initial_pos,
                current_dir=initial_dir,
            )

            if new_guard_map[*last_pos, vec_to_coef(last_dir)] > 1:
                count_loops += 1


print(count_loops)
