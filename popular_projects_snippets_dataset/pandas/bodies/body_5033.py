# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
interval1 = Interval(0, 1, "both")
interval2 = Interval(float("-inf"), float("inf"), "neither")
assert interval1 in interval2
assert interval2 not in interval1
