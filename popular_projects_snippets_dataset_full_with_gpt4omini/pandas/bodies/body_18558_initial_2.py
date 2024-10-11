import numpy as np # pragma: no cover

def roll_qtrday(other, n, month, day_opt, modby=12):# pragma: no cover
    if day_opt == 'start':# pragma: no cover
        return other + (n + month) % modby# pragma: no cover
    return other - (n + month) % modby # pragma: no cover
other = 10 # pragma: no cover
n = 5 # pragma: no cover
expected = {0: 7, 1: 8, 2: 9, 3: 10, 4: 11, 5: 12} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
from l3.Runtime import _l_
month = 3
_l_(10843)
day_opt = "start"  # `other` will be compared to March 1.
_l_(10844)  # `other` will be compared to March 1.

assert roll_qtrday(other, n, month, day_opt, modby=12) == expected[n]
_l_(10845)
