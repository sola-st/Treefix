# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
from l3.Runtime import _l_
month = 3
_l_(22343)
day_opt = "start"  # `other` will be compared to March 1.
_l_(22344)  # `other` will be compared to March 1.

assert roll_qtrday(other, n, month, day_opt, modby=12) == expected[n]
_l_(22345)
