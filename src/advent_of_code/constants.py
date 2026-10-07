"""
Constants for Advent of Code.
"""

import pathlib

PACKAGE_ROOT = pathlib.Path(__file__).parent
assert PACKAGE_ROOT.name == "advent_of_code", (
    "The package root is not 'advent_of_code'"
)

SOLUTIONS_ROOT = PACKAGE_ROOT / "solutions"
