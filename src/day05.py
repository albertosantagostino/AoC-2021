#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

from common.meta_utils import get_puzzle_input


def solve(coordinates, consider_diagonals=False):
    touched_coords = defaultdict(dict)
    for coordinate in coordinates:
        start, end = coordinate[0], coordinate[1]
        if start[0] == end[0]:
            length = abs(start[1] - end[1]) + 1
            y_min = min(start[1], end[1])
            if not start[0] in touched_coords:
                touched_coords[start[0]] = {}
            for y in range(y_min, y_min + length):
                add_point(touched_coords, start[0], y)
        elif start[1] == end[1]:
            length = abs(start[0] - end[0]) + 1
            x_min = min(start[0], end[0])
            for x in range(x_min, x_min + length):
                add_point(touched_coords, x, start[1])
        elif consider_diagonals and start[0] != end[0] and start[1] != end[1]:
            length = abs(start[1] - end[1]) + 1
            if start[0] > end[0]:
                start, end = switcharoo(start, end)
            if start[1] <= end[1]:
                for idx in range(0, length):
                    add_point(touched_coords, start[0] + idx, start[1] + idx)
            else:
                for idx in range(0, length):
                    add_point(touched_coords, start[0] + idx, start[1] - idx)
    count = 0
    for vv in touched_coords.values():
        count = count + sum([1 for val in list(vv.values()) if val >= 2])
    return count


def add_point(touched_coords, new_x, new_y):
    if not new_y in touched_coords[new_x]:
        touched_coords[new_x][new_y] = 1
    else:
        touched_coords[new_x][new_y] = touched_coords[new_x][new_y] + 1


def parse_input(puzzle_input):
    coordinates = []
    for row in puzzle_input:
        row = row.split(' -> ')
        start, end = [int(x) for x in row[0].split(',')
                      ], [int(y) for y in row[1].split(',')]
        coordinates.append((start, end))
    return coordinates


def switcharoo(el1, el2):
    tmp = el1
    el1 = el2
    return el1, tmp


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    coordinates = parse_input(puzzle_input)
    print(f"Part 1 solution: {solve(coordinates)}")
    print(f"Part 2 solution: {solve(coordinates, consider_diagonals=True)}")
