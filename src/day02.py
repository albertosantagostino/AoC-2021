#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import array

from common.meta_utils import get_puzzle_input

SUBMARINE_COMMANDS = {
    'forward': array([1, 0]),
    'down': array([0, 1]),
    'up': array([0, -1])
}


def solve(puzzle_input, consider_aim=False):
    position = array([0, 0])
    aim = 0
    for command in puzzle_input:
        instruction, value = command.split()
        action = SUBMARINE_COMMANDS[instruction]
        if not consider_aim:
            position += (action * int(value))
        else:
            if instruction != 'forward':
                aim += (action * int(value))[1]
            else:
                position += array([int(value), int(value) * aim])
    return position[0] * position[1]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {solve(puzzle_input)}")
    print(f"Part 2 solution: {solve(puzzle_input, consider_aim=True)}")
