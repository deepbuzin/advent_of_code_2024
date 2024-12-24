from collections import defaultdict


with open("input_day11.txt", "r") as f:
    input_str = f.read().strip()

starting_stones = [int(stone) for stone in input_str.split(" ")]
total_steps = 75

descendant_count = defaultdict(lambda: [-1 for _ in range(total_steps + 1)])


def count_descendants(stone: int, cur_step: int, total_steps: int):
    if (
        stone in descendant_count
        and descendant_count[stone][total_steps - cur_step] != -1
    ):
        return descendant_count[stone][total_steps - cur_step]

    if cur_step >= total_steps:
        return 1

    count = 0
    if stone == 0:
        count = count_descendants(1, cur_step + 1, total_steps)
    elif len(str(stone)) % 2 == 0:
        count += count_descendants(
            int(str(stone)[: len(str(stone)) // 2]), cur_step + 1, total_steps
        )
        count += count_descendants(
            int(str(stone)[len(str(stone)) // 2 :]), cur_step + 1, total_steps
        )
    else:
        count = count_descendants(stone * 2024, cur_step + 1, total_steps)

    descendant_count[stone][total_steps - cur_step] = count
    return count


total_stones = 0

for stone in starting_stones:
    total_stones += count_descendants(stone, cur_step=0, total_steps=total_steps)

print(total_stones)

