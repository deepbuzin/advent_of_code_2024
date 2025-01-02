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

for m in machines:
    a = (m.x * m.b_y - m.y * m.b_x) / (m.a_x * m.b_y - m.a_y * m.b_x)
    b = (m.y * m.a_x - m.x * m.a_y) / (m.a_x * m.b_y - m.a_y * m.b_x)
    if a == int(a) and b == int(b):
        total_cost += 3 * a + b

print(int(total_cost))


big_total_cost = 0

for m in machines:
    x = m.x + 10000000000000
    y = m.y + 10000000000000
    a = (x * m.b_y - y * m.b_x) / (m.a_x * m.b_y - m.a_y * m.b_x)
    b = (y * m.a_x - x * m.a_y) / (m.a_x * m.b_y - m.a_y * m.b_x)
    if a == int(a) and b == int(b):
        big_total_cost += 3 * a + b

print(int(big_total_cost))
