import numpy as np
from dataclasses import dataclass
import re


input_str = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

with open("input_day13.txt", "r") as f:
    input_str = f.read().strip()


@dataclass
class Machine:
    a_x: int = 0
    a_y: int = 0
    b_x: int = 0
    b_y: int = 0
    x: int = 0
    y: int = 0


machines = []

for spec in input_str.split("\n\n"):
    machine = Machine()
    lines = spec.strip().split("\n")
    machine.a_x, machine.a_y = [
        int(v) for v in re.findall(r"X\+(\d+?),\s*Y\+(\d+)", lines[0])[0]
    ]
    machine.b_x, machine.b_y = [
        int(v) for v in re.findall(r"X\+(\d+?),\s*Y\+(\d+)", lines[1])[0]
    ]
    machine.x, machine.y = [
        int(v) for v in re.findall(r"X=(\d+?),\s*Y=(\d+)", lines[2])[0]
    ]
    machines.append(machine)


total_cost = 0

for machine in machines:
    dist = np.ones((100, 100, 2)) * np.inf

    for i in range(100):
        for j in range(100):
            dist[i, j] = np.array(
                [
                    float(machine.a_x * i + machine.b_x * j),
                    machine.a_y * i + machine.b_y * j,
                ]
            )

    matches = dist[:, :] == [machine.x, machine.y]
    targets = np.all(matches, axis=-1)
    moves = np.argwhere(targets)
    if len(moves):
        cost = moves[:, 0] * 3 + moves[:, 1]
        total_cost += cost[0]


print(total_cost)
