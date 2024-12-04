import re

with open("input_day3.txt", "r") as f:
    input_str = f.read()

pattern_1 = r"(mul\(([0-9]{1,3}),([0-9]{1,3})\))"
pattern_2 = r"(^|do\(\))(.*?)(don't\(\)|$)"

uncorrupted_1 = 0

for match in re.finditer(pattern_1, input_str):
    uncorrupted_1 += int(match.group(2)) * int(match.group(3))

print(uncorrupted_1)

uncorrupted_2 = 0

for outer_match in re.finditer(pattern_2, input_str, re.DOTALL):
    for inner_match in re.finditer(pattern_1, outer_match.group(2)):
        uncorrupted_2 += int(inner_match.group(2)) * int(inner_match.group(3))

print(uncorrupted_2)

