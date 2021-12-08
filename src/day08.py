#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb

from common.meta_utils import get_puzzle_input


def part1(puzzle_input):
    res = 0
    for display in puzzle_input:
        ciphers = display.split(' | ')[0].split(' ')
        value = display.split(' | ')[1].split(' ')
        vl = [len(el) for el in value]
        res += vl.count(2) + vl.count(3) + vl.count(4) + vl.count(7)
    return res


def part2(puzzle_input):
    ipdb.set_trace()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
