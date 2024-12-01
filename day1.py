from collections import defaultdict


with open("input_day1.txt", "r") as f:
    input = f.readlines()

left_list = sorted([int(line.split("   ")[0]) for line in input])
right_list = sorted([int(line.split("   ")[1]) for line in input])

sum = 0

for left, right in zip(left_list, right_list):
    sum += abs(left - right)

print(sum)

counts = defaultdict(int)

for right in right_list:
    counts[right] += 1

similarity = 0

for left in left_list:
    similarity += left * counts.get(left, 0)

print(similarity)
