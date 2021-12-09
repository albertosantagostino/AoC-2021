#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb
import numpy as np

from common.meta_utils import get_puzzle_input


def part1(heightmap):
    low_points = calculate_heightmap_low_points(heightmap)
    return sum([value + 1 for value in low_points.values()])


def part2(puzzle_input):
    #return res
    ipdb.set_trace()


def calculate_heightmap_low_points(heightmap):
    rows, cols = heightmap.shape
    low_points = {}
    for row in range(0, rows):
        for col in range(0, cols):
            val = heightmap[row, col]
            val_l = val_r = val_d = val_u = 9999
            if row - 1 >= 0:
                val_l = heightmap[row - 1, col]
            if row + 1 < rows:
                val_r = heightmap[row + 1, col]
            if col - 1 >= 0:
                val_u = heightmap[row, col - 1]
            if col + 1 < cols:
                val_d = heightmap[row, col + 1]
            if (val < val_l) and (val < val_r) and (val < val_u) and (val <
                                                                      val_d):
                low_points[(row, col)] = val
    return low_points


def parse_input(puzzle_input):
    puzzle_input = [[int(el) for el in row] for row in puzzle_input]
    return np.matrix(puzzle_input)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    heightmap = parse_input(puzzle_input)
    print(f"Part 1 solution: {part1(heightmap)}")
    #print(f"Part 2 solution: {part2(puzzle_input)}")
