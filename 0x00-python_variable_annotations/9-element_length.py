#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values
with the appropriate types.

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate function param
    element_length
    """
    return [(i, len(i)) for i in lst]
