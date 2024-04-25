#!/usr/bin/env python3
"""9"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function’s parameters"""
    return [(i, len(i)) for i in lst]
