import numpy as np


with open("input_day9.txt", "r") as f:
    input_str = f.read().strip()

input_nums = [int(c) for c in input_str]

reverse_files = []

for i in range(1, len(input_nums) + 1, 2):
    count = input_nums[-i]
    idx = (len(input_nums) - i + 1) // 2
    for _ in range(count):
        reverse_files.append(idx)

len_all_files = sum([input_nums[i] for i in range(0, len(input_nums), 2)])

fs_position = 0
reverse_fs_position = 0

result_fs = []
checksum = 0

for i, count in enumerate(input_nums):
    if i % 2 == 0:
        # count is file
        file_idx = i // 2
        for _ in range(count):
            if fs_position >= len_all_files:
                break
            result_fs.append(file_idx)
            checksum += file_idx * fs_position
            fs_position += 1
    else:
        # count is empty space
        for _ in range(count):
            if fs_position >= len_all_files:
                break
            result_fs.append(reverse_files[reverse_fs_position])
            checksum += reverse_files[reverse_fs_position] * fs_position
            fs_position += 1
            reverse_fs_position += 1

print(checksum)

disk_map = np.array(input_nums)
start_indices = disk_map.cumsum()
full_map = np.zeros(disk_map.sum())

for i, count in enumerate(disk_map):
    if i % 2 == 0:
        start = start_indices[i - 1]
        full_map[start : start + count] = i // 2


for map_offset in range(0, len(disk_map), 2):
    file_loc = len(disk_map) - map_offset - 1
    count = disk_map[file_loc]

    old_pos = disk_map.cumsum()[file_loc - 1]
    slice = full_map[old_pos : old_pos + count] 
    val = full_map[old_pos]

    for space_idx in range(1, len(disk_map) - 1 - map_offset, 2):
        if disk_map[space_idx] >= disk_map[file_loc]:
            full_map[old_pos : old_pos + count] = 0

            new_pos = disk_map.cumsum()[space_idx - 1]
            full_map[new_pos : new_pos + count] = val

            disk_map[space_idx] -= count
            disk_map = np.insert(disk_map, space_idx, [0, count])
            break

defrag_checksum =  sum(full_map * np.array(list(range(len(full_map)))))
print(defrag_checksum)


