#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb

from common.meta_utils import get_puzzle_input


def part1(puzzle_input):
    par_opener = '([{<'
    par_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    par_opener_lookup = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<',
    }
    illegal_pars = []
    corrupted_lines_idx = []
    for idx, line in enumerate(puzzle_input):
        par_stack = []
        for char in line:
            if char not in par_opener_lookup.values():
                if not par_stack:
                    illegal_pars.append(char)
                    corrupted_lines_idx.append(idx)
                    break
                last_par = par_stack.pop()
                if last_par != par_opener_lookup[char]:
                    illegal_pars.append(char)
                    corrupted_lines_idx.append(idx)
                    break
            else:
                par_stack.append(char)
    return corrupted_lines_idx, sum([par_score[char] for char in illegal_pars])


def part2(incomplete_lines):
    #return res
    ipdb.set_trace()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    corrupted_lines_idx, res_part1 = part1(puzzle_input)
    print(f"Part 1 solution: {res_part1}")
    excluded_itemgetter = lambda idx, seq: [
        v for i, v in enumerate(seq) if i not in set(idx)
    ]
    incomplete_lines = (excluded_itemgetter(corrupted_lines_idx, puzzle_input))
    print(f"Part 2 solution: {part2(incomplete_lines)}")
