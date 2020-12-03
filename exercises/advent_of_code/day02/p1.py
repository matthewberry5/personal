"""Advent of Coding Day 2.
Part 1: Find the amount of valid passwords.
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
        range1: int = get_range1(line)
        range2: int = get_range2(line)
        golden_char: str = get_golden(line)
        occur: int = get_occur(line, golden_char)
        if occur >= range1 and occur <= range2:
            valid += 1
        else: 
            invalid += 1
    print(f"There are {valid} valid passwords and {invalid} invalid passwords.")
    file_handle.close()


def get_range1(report: str) -> int:
    output: str = ""
    i: int = 0
    while report[i] != "-":
        output += report[i]
        i += 1
    return int(output)


def get_range2(report: str) -> int:
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


def get_occur(report: str, golden: str) -> int:
    counts: int = 0
    i: int = 0
    while report[i] != ":":
        i += 1
    for j in range(i, len(report)):
        if report[j] == golden:
            counts += 1
    return counts


if __name__ == "__main__":
    main()