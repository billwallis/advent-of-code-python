"""
Day 23: LAN Party

https://adventofcode.com/2024/day/23
"""

from __future__ import annotations

import logging
import pathlib

from advent_of_code.meta import read_input


def solution(use_sample: bool) -> list:
    """
    Solve the day 23 problem!
    """

    logging.basicConfig(level="DEBUG")
    file = "sample.data" if use_sample else "input.data"
    input_ = read_input(pathlib.Path(__file__).parent / file)

    return [
        0,
        0,
    ]
