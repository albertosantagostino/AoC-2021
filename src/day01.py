#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input


def part1(puzzle_input):
    return count_increments(puzzle_input)


def part2(puzzle_input):
    reduced_input = reduce_sum_sliding_window(puzzle_input, width=3)
    return count_increments(reduced_input)


def count_increments(values):
    count = 0
    for idx in range(0, len(values) - 1):
        if values[idx + 1] - values[idx] > 0:
            count = count + 1
    return count


def reduce_sum_sliding_window(values, width):
    new_values = []
    for idx in range(0, len(values) - width + 1):
        new_values.append(sum(values[idx:idx + width]))
    return new_values


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__, cast=int)
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
