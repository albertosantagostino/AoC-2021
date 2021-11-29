#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

from pathlib import Path

root_path = Path(__file__).parents[2]
config = json.load(root_path.joinpath('config.json').open())


def download_puzzle_data(year, day):
    print(f"Fetching puzzle input for day {day}")
    res = requests.get(url=f'https://adventofcode.com/{year}/day/{day}/input',
                       cookies={"session": config['aoc_cookie']})
    res.raise_for_status()
    with open(root_path.joinpath('data', f'day{day}_input.txt'), 'w') as fp:
        fp.write(res.text)


def get_filename_day(file_path):
    return int(file_path.split('/')[-1][3:5])


def get_puzzle_data(day):
    puzzle_input = root_path.joinpath('data', f'day{day}_input.txt')
    if not puzzle_input.exists():
        download_puzzle_data(year=config['year'], day=day)

    return puzzle_input.open().read().splitlines()
