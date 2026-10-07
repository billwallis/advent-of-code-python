<span align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![tests](https://github.com/billwallis/advent-of-code-python/actions/workflows/tests.yaml/badge.svg)](https://github.com/billwallis/advent-of-code-python/actions/workflows/tests.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/billwallis/advent-of-code-python/main.svg)](https://results.pre-commit.ci/latest/github/billwallis/advent-of-code-python/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/billwallis/advent-of-code-python)](https://shields.io/badges/git-hub-last-commit)

</span>

---

# Advent of Code - Python

Python solutions to the Advent of Code problem sets, available at:

- [https://adventofcode.com/](https://adventofcode.com/)

This is just an opportunity for me to work on my OOP, so the solutions are not optimal.

## Contributing

Install the dependencies:

```shell
# Setup
pip install --editable . --group dev --group test
pre-commit install --install-hooks

# Use the CLI
aoc --help
```

Create an `.env` file with the session cookie you get from Advent of Code:

```
AOC_SESSION_COOKIE="session=..."
```

You can find the session cookie in your browser's developer tools after logging in to [Advent of Code](https://adventofcode.com/).
