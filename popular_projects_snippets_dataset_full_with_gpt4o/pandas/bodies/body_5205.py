# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# The td fixture should always be far from the implementation
#  bound, so doubling does not risk overflow.
res = td * 2
assert res.value == td.value * 2
assert res._creso == unit
