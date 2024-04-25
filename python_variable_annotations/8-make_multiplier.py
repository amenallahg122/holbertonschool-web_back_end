#!/usr/bin/env python3
"""8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by multiplier"""

    def multiply(number: float) -> float:
        """multiplies a float by multiplier"""
        return number * multiplier

    return multiply
