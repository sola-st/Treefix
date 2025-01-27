# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#13624 for str
box = box_with_array

rng = timedelta_range("1 days", periods=10)
obj = tm.box_expected(rng, box)

assert_invalid_comparison(obj, invalid, box)
