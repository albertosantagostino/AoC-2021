#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb

from common.meta_utils import get_puzzle_input


# Position is expressed as [horizontal, depth] or as [x, -z]
class SubmarinePosition():
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def __repr__(self):
        return f"SubmarinePosition({self.x}, {self.z})"

    def __str__(self):
        return SubmarinePosition(self.x, self.z)

    def __add__(self, other):
        return SubmarinePosition(self.x + other.x, self.z + other.z)

    def __mul__(self, other):
        if isinstance(other, int):
            return SubmarinePosition(self.x * other, self.z * other)


SUBMARINE_COMMANDS_V1 = {
    'forward': SubmarinePosition(1, 0),
    'down': SubmarinePosition(0, 1),
    'up': SubmarinePosition(0, -1)
}


def part1(puzzle_input):
    position = SubmarinePosition(0, 0)
    for command in puzzle_input:
        instruction, value = command.split()
        value = int(value)
        try:
            action = SUBMARINE_COMMANDS_V1[instruction]
        except KeyError:
            raise KeyError(f"Unknown command ({instruction})")
        position = position + (action * value)
    return position.x * position.z


def part2(puzzle_input):
    position = SubmarinePosition(0, 0)
    aim = 0
    for command in puzzle_input:
        instruction, value = command.split()
        value = int(value)
        if instruction == 'down':
            aim = aim + value
        elif instruction == 'up':
            aim = aim - value
        elif instruction == 'forward':
            position = position + SubmarinePosition(value, value * aim)
    return position.x * position.z


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
