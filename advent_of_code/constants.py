"""
Constants for Advent of Code.
"""

import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
assert PROJECT_ROOT.name == "advent-of-code-python", (
    "The project root is not 'advent-of-code-python'"
)

SOLUTIONS_ROOT = PROJECT_ROOT / "advent_of_code/solutions"
