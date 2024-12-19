input_str = """
2333133121414131402
""".strip()

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
    

print(reverse_files)
print(result_fs)
print(checksum)

