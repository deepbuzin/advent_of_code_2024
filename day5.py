from collections import defaultdict


with open("input_day5.txt", "r") as f:
    input_str = f.read().strip()

ordering_str, updates_str = input_str.split("\n\n")

order_map = defaultdict(list)

for pair in ordering_str.split("\n"):
    before, after = [int(page) for page in pair.split("|")]
    order_map[after].append(before)

updates = []

for line in updates_str.split("\n"):
    updates.append([int(page) for page in line.split(",")])

correct_sum = 0
incorrect_sum = 0

for update in updates:
    is_correct = True
    for i, page_current in enumerate(update):
        for page_next in update[i:]:
            if page_next in order_map[page_current]:
                is_correct = False
                break
    if is_correct:
        correct_sum += update[len(update) // 2]
    else:
        for i in range(len(update)):
            for j in range(i, len(update)):
                if update[j] in order_map[update[i]]:
                    tmp = update[i]
                    update[i] = update[j]
                    update[j] = tmp
        
        incorrect_sum += update[len(update) // 2]


print(correct_sum)
print(incorrect_sum)
