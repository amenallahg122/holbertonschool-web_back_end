#!/usr/bin/env python3
"""5"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums the elements of a list
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
