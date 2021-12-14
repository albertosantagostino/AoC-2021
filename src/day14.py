#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb

from common.meta_utils import get_puzzle_input

from collections import Counter


def part1(polymer, rules):
    for step in range(0, 10):
        char_to_insert = {}
        polymer_pairs = [
            el[0] + el[1] for el in list(zip(polymer, polymer[1:]))
        ]
        for idx, pair in enumerate(polymer_pairs):
            try:
                char_to_insert[idx] = rules[pair]
            except KeyError:
                pass
        for idx, char in char_to_insert.items():
            polymer_pairs[
                idx] = polymer_pairs[idx][0] + char + polymer_pairs[idx][1]
        polymer = '' + polymer_pairs[0]
        for idx in range(1, len(polymer_pairs)):
            polymer += polymer_pairs[idx][1:]
    char_frequency = Counter(polymer)
    return max(char_frequency.values()) - min(char_frequency.values())


def part2(polymer, rules):
    #return res
    ipdb.set_trace()


def parse_input(puzzle_input):
    rules = {}
    polymer = puzzle_input[0]
    for idx in range(2, len(puzzle_input)):
        start, end = puzzle_input[idx].split(' -> ')
        rules[start] = end
    return polymer, rules


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    polymer, rules = parse_input(puzzle_input)
    print(f"Part 1 solution: {part1(polymer, rules)}")
    print(f"Part 2 solution: {part2(polymer, rules)}")
