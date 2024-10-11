# Extracted from https://stackoverflow.com/questions/37835179/how-can-i-specify-the-function-type-in-my-type-hints
from typing import Callable

def my_function(func: Callable):

def sum(a: int, b: int) -> int: return a+b

Callable[[int, int], int]

Callable[[ParamType1, ParamType2, .., ParamTypeN], ReturnType]

