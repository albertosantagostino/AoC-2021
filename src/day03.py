#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.meta_utils import get_puzzle_input


def part1(puzzle_input):
    gamma_rate = ''
    for bit in range(0, len(puzzle_input[0])):
        count = 0
        for number in puzzle_input:
            count = count + int(number[bit])
        if count > len(puzzle_input) / 2:
            gamma_rate += '1'
        else:
            gamma_rate += '0'
    epsilon_rate = ''.join('0' if idx == '1' else '1' for idx in gamma_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(puzzle_input):
    o2_rating = reduce_lists_part2(puzzle_input)
    co2_rating = reduce_lists_part2(puzzle_input, keep_0s=True)
    return o2_rating * co2_rating


def reduce_lists_part2(numbers, keep_0s=False):
    for bit in range(0, len(numbers[0])):
        count = 0
        for number in range(0, len(numbers)):
            count = count + int(numbers[number][bit])
        if keep_0s:
            keep = str(int(not count >= len(numbers) / 2))
        else:
            keep = str(int(count >= len(numbers) / 2))
        numbers = [el for el in numbers if el[bit] == keep]
        if len(numbers) == 1:
            break
    return int(numbers[0], 2)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(puzzle_input)}")
    print(f"Part 2 solution: {part2(puzzle_input)}")
