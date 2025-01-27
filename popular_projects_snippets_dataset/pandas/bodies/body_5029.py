# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
start, shift = start_shift
interval1 = Interval(start, start + shift, other_closed)
interval2 = Interval(start + 2 * shift, start + 3 * shift, closed)

# disjoint intervals should never overlap
assert not interval1.overlaps(interval2)
