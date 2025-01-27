# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
assert abs(td)._creso == unit
assert (-td)._creso == unit
assert (+td)._creso == unit
