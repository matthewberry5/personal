"""Advent of Coding Day 2
Part 2: Find the amount of valid passwords under new policy.
"""

__author__ = "matthewberry5"


from typing import List, Dict
import sys


cli_handle = sys.argv[1]
file_handle = open(cli_handle)


def main() -> None:
    table: List[str] = []
    for line in file_handle:
        table.append(line)
    valid: int = 0
    invalid: int = 0
    for line in table: 
        pos1: int = get_pos1(line)
        pos2: int = get_pos2(line)
        golden_char: str = get_golden(line)
        occur: int = get_occur(line, golden_char, pos1, pos2)
        if occur == 1: 
            valid += 1
        else: 
            invalid += 1
    print(f"There are {valid} valid passwords and {invalid} invalid passwords.")
    file_handle.close()


def get_pos1(report: str) -> int:
    output: str = ""
    i: int = 0
    while report[i] != "-":
        output += report[i]
        i += 1
    return int(output)


def get_pos2(report: str) -> int:
    output: str = ""
    i: int = 0
    while report[i] != "-":
        i += 1 
    while report[i] != " ":
        if report[i] != "-":
            output += report[i]
        i += 1
    return int(output)


def get_golden(report: str) -> str:
    output: str = ""
    i: int = 0
    while report[i] != " ":
        i += 1
    while report[i] != ":": 
        if report[i] != " ":
            output += report[i]
        i += 1
    return output


def get_occur(report: str, golden: str, option1: int, option2: int) -> int:
    counts: int = 0
    i: int = 0
    while report[i] != ":":
        i += 1
    if report[option1 + i + 1] == golden:
        counts += 1
    if report[option2 + i + 1] == golden:
        counts += 1
    return counts


if __name__ == "__main__":
    main()