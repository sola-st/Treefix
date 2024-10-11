# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
start, shift = start_shift
interval1 = Interval(start, start + shift, other_closed)
interval2 = Interval(start + shift, start + 2 * shift, closed)

# overlap if shared endpoint is closed for both (overlap at a point)
result = interval1.overlaps(interval2)
expected = interval1.closed_right and interval2.closed_left
assert result == expected
