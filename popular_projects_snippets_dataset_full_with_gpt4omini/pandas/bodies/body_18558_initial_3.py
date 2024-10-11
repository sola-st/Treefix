def roll_qtrday(other, n, month, day_opt, modby): # pragma: no cover
    # Example implementation just for demonstration # pragma: no cover
    return other + n + month, day_opt # pragma: no cover
expected = {0: (10, 'start'), 1: (11, 'start'), 2: (12, 'start')} # pragma: no cover

other = 7 # pragma: no cover
n = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
from l3.Runtime import _l_
month = 3
_l_(10843)
day_opt = "start"  # `other` will be compared to March 1.
_l_(10844)  # `other` will be compared to March 1.

assert roll_qtrday(other, n, month, day_opt, modby=12) == expected[n]
_l_(10845)
