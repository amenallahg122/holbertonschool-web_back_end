#!/usr/bin/env python3
"""Return function that multiplies float by `multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by multiplier"""

    def multiply(number: float) -> float:
        """multiplies a float by multiplier"""
        return number * multiplier

    return multiply
