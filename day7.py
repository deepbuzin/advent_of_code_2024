from typing import List


with open("input_day7.txt", "r") as f:
    input_str = f.read().strip()

equations = []

for equation in input_str.split("\n"):
    target, terms = equation.split(":")
    equations.append(
        {
            "target": int(target),
            "terms": [int(term) for term in terms.strip().split(" ")],
        }
    )


def dfs(current_total: int, current_idx: int, target: int, terms: List[int]) -> bool:
    if current_idx >= len(terms):
        return current_total == target

    add = current_total + terms[current_idx]
    mult = current_total * terms[current_idx]

    return (add <= target and dfs(add, current_idx + 1, target, terms)) or (
        mult <= target and dfs(mult, current_idx + 1, target, terms)
    )


total_calibration_result = 0

for equation in equations:
    is_possible = dfs(current_total=equation["terms"][0], current_idx=1, **equation)
    if is_possible:
        total_calibration_result += equation["target"]

print(total_calibration_result)


def concat(left: int, right: int) -> int:
    return int(str(left) + str(right))


def dfs_with_concat(target: int, terms: List[int]) -> bool:
    if len(terms) == 1:
        return terms[0] == target

    add_branch = dfs_with_concat(target, [terms[0] + terms[1], *terms[2:]])
    mult_branch = dfs_with_concat(target, [terms[0] * terms[1], *terms[2:]])
    concat_branch = dfs_with_concat(target, [concat(terms[0], terms[1]), *terms[2:]])

    return add_branch or mult_branch or concat_branch


total_concat = 0

for equation in equations:
    # for equation in equations:
    is_possible = dfs_with_concat(**equation)
    if is_possible:
        total_concat += equation["target"]

print(total_concat)
