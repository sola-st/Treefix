# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
interval1 = Interval(0, 1, "both")
interval2 = Interval(-1, -1, "both")
interval3 = Interval(0.5, 0.5, "both")
assert interval2 not in interval1
assert interval3 in interval1
assert interval2 not in interval3 and interval3 not in interval2
assert interval1 not in interval2 and interval1 not in interval3
