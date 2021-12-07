#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input


def part1(puzzle_input):
    median = puzzle_input[int((len(puzzle_input) + 1) / 2)]
    return sum([abs(el - median) for el in puzzle_input])


def part2(puzzle_input):
    lookup_fuel = {
        kk: sum([vv for vv in range(0, kk + 1)])
        for kk in range(0, max(puzzle_input))
    }
    get_fuel = lambda lookup_fuel, test_value: sum(
        [lookup_fuel[abs(el - test_value)] for el in puzzle_input])
    min_fuel = 99999999
    for test_value in range(1, max(puzzle_input)):
        fuel = get_fuel(lookup_fuel, test_value)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__, cast=int, oneline=True)
    puzzle_input.sort()
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
