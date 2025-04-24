#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable of sequences.
    
    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing each sequence and its length
    """
    return [(i, len(i)) for i in lst] 