#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

from copy import deepcopy
from functools import reduce

from common.meta_utils import get_puzzle_input


def part1(extracted_numbers, boards):
    while extracted_numbers:
        number = extracted_numbers.pop(0)
        if res := mark_number_and_check(number, boards):
            return list(res.values())[0]


def part2(extracted_numbers, boards):
    n_boards = list(range(0, len(boards)))
    scores = []
    while n_boards and extracted_numbers:
        number = extracted_numbers.pop(0)
        if res := mark_number_and_check(number, boards):
            for kk, vv in res.items():
                if kk in n_boards:
                    n_boards.remove(kk)
                    scores.append(vv)
                    del boards[kk]
    return scores[-1]


def mark_number_and_check(extracted_number, boards):
    winners = {}
    for kk, vv in boards.items():
        if extracted_number in vv:
            vv[np.where(vv == extracted_number)] = -1
            sum_cols = np.sum(vv, axis=0)
            sum_rows = np.sum(vv, axis=1)
            if -5 in sum_cols or -5 in sum_rows:
                winners[kk] = calculate_board_sum(vv) * extracted_number
    return winners


def calculate_board_sum(board):
    new_board = deepcopy(board)
    new_board[new_board < 0] = 0
    return np.sum(new_board)


def parse_input(puzzle_input):
    extracted_numbers = puzzle_input.pop(0).split(',')
    extracted_numbers = [int(val) for val in extracted_numbers]
    puzzle_input = list(filter(None, puzzle_input))
    boards = {}
    for idx in range(0, int(len(puzzle_input) / 5)):
        board = puzzle_input[idx * 5:(idx * 5) + 5]
        boards[idx] = np.matrix(reduce(lambda x, y: x + ';' + y, board))
    return extracted_numbers, boards


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    extracted_numbers, boards = parse_input(puzzle_input)
    print(
        f"Part 1 solution: {part1(deepcopy(extracted_numbers), deepcopy(boards))}"
    )
    print(
        f"Part 2 solution: {part2(deepcopy(extracted_numbers), deepcopy(boards))}"
    )
