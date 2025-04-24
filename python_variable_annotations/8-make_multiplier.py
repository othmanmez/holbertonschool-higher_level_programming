#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a multiplier.
    
    Args:
        multiplier (float): The multiplier to use
        
    Returns:
        Callable[[float], float]: A function that takes a float and returns a float
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply 