# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
interval1 = Interval(0, 1, "both")
interval2 = Interval(0, 1, inclusive_endpoints_fixture)
assert interval1 in interval1
assert interval2 in interval2
assert interval2 in interval1
assert interval1 not in interval2 or inclusive_endpoints_fixture == "both"
