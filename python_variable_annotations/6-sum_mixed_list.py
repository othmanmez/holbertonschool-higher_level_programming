#!/usr/bin/env python3

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.
    
    Args:
        mxd_lst (List[Union[int, float]]): List of integers and floats
        
    Returns:
        float: Sum of all elements in the list
    """
    return sum(mxd_lst) 