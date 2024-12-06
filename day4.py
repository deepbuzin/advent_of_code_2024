import re


with open("input_day4.txt") as f:
    input_str = f.read().strip()

matrix = []

for i, row in enumerate(input_str.split("\n")):
    matrix.append([])
    for letter in row:
        matrix[i].append(letter)

num_diag = max(len(matrix), len(matrix[0]))
rows, cols = len(matrix), len(matrix[0])

lines = []

for row in matrix:
    lines.append("".join(row))

for col in range(cols):
    lines.append("".join([row[col] for row in matrix]))

for offset in range(-num_diag, num_diag):
    if offset >= 0:
        diag = [matrix[i][i + offset] for i in range(min(rows, cols - offset))]
    else:
        diag = [matrix[i - offset][i] for i in range(min(rows + offset, cols))]
    lines.append("".join(diag))


for offset in range(-num_diag, num_diag):
    if offset >= 0:
        anti_diag = [
            matrix[i][cols - i - offset - 1] for i in range(min(rows, cols - offset))
        ]
    else:
        anti_diag = [
            matrix[i - offset][cols - i - 1] for i in range(min(rows + offset, cols))
        ]

    lines.append("".join(anti_diag))

xmas_count = 0

reverse_lines = [line[::-1] for line in lines]

for line in lines + reverse_lines:
    xmas_count += line.count("XMAS")

print(xmas_count)


pattern = "M(AS)"


def get_match_indices(diag):
    line = "".join(diag)
    mas_indices = [match.start(1) for match in re.finditer(pattern, line)]
    reverse_mas_indices = [
        len(line) - 1 - match.start(1) for match in re.finditer(pattern, line[::-1])
    ]
    return mas_indices + reverse_mas_indices


diag_mases = []

for offset in range(-num_diag, num_diag):
    if offset >= 0:
        diag = [matrix[i][i + offset] for i in range(min(rows, cols - offset))]
        mas_indices = get_match_indices(diag)
        diag_mases.extend([(i, i + offset) for i in mas_indices])
    else:
        diag = [matrix[i - offset][i] for i in range(min(rows + offset, cols))]
        mas_indices = get_match_indices(diag)
        diag_mases.extend([(i - offset, i) for i in mas_indices])


anti_diag_mases = []

for offset in range(-num_diag, num_diag):
    if offset >= 0:
        anti_diag = [
            matrix[i][cols - i - offset - 1] for i in range(min(rows, cols - offset))
        ]
        mas_indices = get_match_indices(anti_diag)
        anti_diag_mases.extend([(i, cols - i - offset - 1) for i in mas_indices])
    else:
        anti_diag = [
            matrix[i - offset][cols - i - 1] for i in range(min(rows + offset, cols))
        ]
        mas_indices = get_match_indices(anti_diag)
        anti_diag_mases.extend([(i - offset, cols - i - 1) for i in mas_indices])

x_mas_count = 0
for pair in anti_diag_mases:
    if pair in diag_mases:
        x_mas_count += 1

print(x_mas_count)
