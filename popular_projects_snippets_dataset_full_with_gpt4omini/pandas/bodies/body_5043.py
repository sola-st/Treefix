# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
assert Interval(0, 1) == Interval(0, 1, closed="right")
assert Interval(0, 1) != Interval(0, 1, closed="left")
assert Interval(0, 1) != 0
