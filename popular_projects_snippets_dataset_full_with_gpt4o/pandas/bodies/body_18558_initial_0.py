def roll_qtrday(other, n, month, day_opt, modby=12): # pragma: no cover
    if day_opt == 'start': # pragma: no cover
        base_day = 1 # pragma: no cover
    else: # pragma: no cover
        base_day = other # pragma: no cover
    new_day = (base_day + n) % modby # pragma: no cover
    return new_day # pragma: no cover
 # pragma: no cover
other = 1 # pragma: no cover
n = 2 # pragma: no cover
expected = {2: 3, 4: 5, 6: 7, 8: 9} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
from l3.Runtime import _l_
month = 3
_l_(22343)
day_opt = "start"  # `other` will be compared to March 1.
_l_(22344)  # `other` will be compared to March 1.

assert roll_qtrday(other, n, month, day_opt, modby=12) == expected[n]
_l_(22345)
