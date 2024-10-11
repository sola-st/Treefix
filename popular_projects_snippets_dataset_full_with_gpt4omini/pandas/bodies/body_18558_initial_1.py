from typing import List # pragma: no cover

def roll_qtrday(other: int, n: int, month: int, day_opt: str, modby: int) -> int: return (other + n) % modby # pragma: no cover
other = 1 # pragma: no cover
n = 5 # pragma: no cover
expected = [6, 7, 8, 9, 10, 11] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
from l3.Runtime import _l_
month = 3
_l_(10843)
day_opt = "start"  # `other` will be compared to March 1.
_l_(10844)  # `other` will be compared to March 1.

assert roll_qtrday(other, n, month, day_opt, modby=12) == expected[n]
_l_(10845)
