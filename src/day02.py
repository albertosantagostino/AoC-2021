#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import array

from common.meta_utils import get_puzzle_input

SUBMARINE_COMMANDS = {
    'forward': array([1, 0]),
    'down': array([0, 1]),
    'up': array([0, -1])
}


def part1(puzzle_input):
    position = array([0, 0])
    for command in puzzle_input:
        instruction, value = command.split()
        action = SUBMARINE_COMMANDS[instruction]
        position = position + (action * int(value))
    return position[0] * position[1]


def part2(puzzle_input):
    position = array([0, 0])
    aim = 0
    for command in puzzle_input:
        instruction, value = command.split()
        value = int(value)
        action = SUBMARINE_COMMANDS[instruction]
        if instruction != 'forward':
            aim = aim + (action * int(value))[1]
        else:
            position = position + array([value, value * aim])
    return position[0] * position[1]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
