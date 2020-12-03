"""Advent of Code problem 1.
Goal 1: Find the two entries that sum to 2020;
what do you get if you multiply them together?

Goal 2: Find the three entries that sum to 2020;
what do you get if you multiply them together?
"""

__author__ = "matthewberry5"


from typing import List
import sys

cli_handle = sys.argv[1]
file_handle = open(cli_handle)

def main() -> None:
    table: List[int] = []
    for line in file_handle: 
        table.append(int(line))
    two_values: List[int] = find_two(table)
    two_answer: int = 1
    for i in range(0, len(two_values)):
        two_answer *= two_values[i]
    three_values: List[int] = find_three(table)
    three_answer: int = 1
    for i in range(0, len(three_values)):
        three_answer *= three_values[i]
    print(f"The product of the two values is {two_answer}")
    print(f"The product of the three values is {three_answer}")
    

def find_two(report: List[int]) -> List[int]:
    for row in report:
        for i in range(1, len(report)):
            if row + report[i] == 2020:
                return [row, report[i]]


def find_three(report: List[int]) -> List[int]:
    for row in report:
        for i in range(1, len(report)):
            for j in range(2, len(report)):
                if row + report[i] + report[j] == 2020:
                    return [row, report[i], report[j]]
                
if __name__ == "__main__":
    main()                