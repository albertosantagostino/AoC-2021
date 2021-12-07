#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input


def solve(puzzle_input, days):
    fish = {kk: 0 for kk in range(0, 9)}
    for fish_age in puzzle_input:
        fish[fish_age] += 1
    for i in range(0, days):
        step(fish)
    return sum(fish.values())


def step(fish):
    new_spawns = 0
    for kk in fish.keys():
        if kk == 0 and fish[kk]:
            new_spawns = fish[kk]
        elif fish[kk]:
            fish[kk - 1] += fish[kk]
        fish[kk] = 0
    fish[8] += new_spawns
    fish[6] += new_spawns


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__, cast=int, oneline=True)
    print(f"Part 1 solution: {solve(puzzle_input, days=80)}")
    print(f"Part 2 solution: {solve(puzzle_input, days=256)}")
