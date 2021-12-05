#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb

from collections import defaultdict

from common.meta_utils import get_puzzle_input


def part1(coordinates):
    touched_coords = defaultdict(dict)
    for coordinate in coordinates:
        start, end = coordinate[0], coordinate[1]
        if start[0] == end[0]:
            # Vertical line
            length = abs(start[1] - end[1]) + 1
            y_min = min(start[1], end[1])
            if not start[0] in touched_coords:
                touched_coords[start[0]] = {}
            for y in range(y_min, y_min + length):
                if not y in touched_coords[start[0]]:
                    touched_coords[start[0]][y] = 1
                else:
                    touched_coords[
                        start[0]][y] = touched_coords[start[0]][y] + 1
        elif start[1] == end[1]:
            # Horizontal line
            length = abs(start[0] - end[0]) + 1
            x_min = min(start[0], end[0])
            for x in range(x_min, x_min + length):
                if not start[0] in touched_coords:
                    touched_coords[start[0]] = {}
                if not start[1] in touched_coords[x]:
                    touched_coords[x][start[1]] = 1
                else:
                    touched_coords[x][
                        start[1]] = touched_coords[x][start[1]] + 1

    count = 0
    for kk, vv in touched_coords.items():
        count = count + sum([1 for val in list(vv.values()) if val >= 2])
    return count


def part2(coordinates):
    #return res
    ipdb.set_trace()


def parse_input(puzzle_input):
    coordinates = []
    for row in puzzle_input:
        row = row.split(' -> ')
        start, end = [int(x) for x in row[0].split(',')
                      ], [int(y) for y in row[1].split(',')]
        coordinates.append((start, end))
    return coordinates


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    coordinates = parse_input(puzzle_input)
    print(f"Part 1 solution: {part1(coordinates)}")
    print(f"Part 2 solution: {part2(coordinates)}")
