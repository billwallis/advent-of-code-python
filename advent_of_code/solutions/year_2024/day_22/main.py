"""
Day 22: Monkey Market

https://adventofcode.com/2024/day/22
"""

from __future__ import annotations

import logging
import pathlib

from advent_of_code.meta import read_input


def solution(use_sample: bool) -> list:
    """
    Solve the day 22 problem!
    """

    logging.basicConfig(level="DEBUG")
    file = "sample-1.data" if use_sample else "input.data"
    input_ = read_input(pathlib.Path(__file__).parent / file)

    return [
        0,
        0,
    ]
