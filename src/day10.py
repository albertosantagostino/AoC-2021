#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input

par_lookup = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<',
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}
par_score_part1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
par_score_part2 = {')': 1, ']': 2, '}': 3, '>': 4}


def part1(puzzle_input):
    illegal_pars = []
    corrupted_lines_idx = []
    for idx, line in enumerate(puzzle_input):
        par_stack = []
        for char in line:
            if char not in '([{<':
                if not par_stack:
                    illegal_pars.append(char)
                    corrupted_lines_idx.append(idx)
                    break
                last_par = par_stack.pop()
                if last_par != par_lookup[char]:
                    illegal_pars.append(char)
                    corrupted_lines_idx.append(idx)
                    break
            else:
                par_stack.append(char)
    return corrupted_lines_idx, sum(
        [par_score_part1[char] for char in illegal_pars])


def part2(incomplete_lines):
    scoreboard = []
    for line in incomplete_lines:
        while True:
            last_length = len(line)
            for combo in ['()', '[]', '{}', '<>']:
                line = line.replace(combo, '')
            if last_length == len(line):
                break
        missing_par = ''.join([par_lookup[char] for char in line[::-1]])
        scoreboard.append(compute_completion_score(missing_par))
    scoreboard.sort()
    return scoreboard[int(len(scoreboard) / 2)]


def compute_completion_score(missing_par):
    score = 0
    for char in missing_par:
        score = score * 5 + par_score_part2[char]
    return score


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    corrupted_lines_idx, res_part1 = part1(puzzle_input)
    print(f"Part 1 solution: {res_part1}")
    excluded_itemgetter = lambda idx, seq: [
        v for i, v in enumerate(seq) if i not in set(idx)
    ]
    incomplete_lines = (excluded_itemgetter(corrupted_lines_idx, puzzle_input))
    print(f"Part 2 solution: {part2(incomplete_lines)}")
