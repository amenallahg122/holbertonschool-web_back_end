#!/usr/bin/env python3
"""7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A list of tuples with the square of the value"""
    return (k, v**2)
