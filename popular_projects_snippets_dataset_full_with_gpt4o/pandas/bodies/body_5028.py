# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
start, shift = start_shift
interval1 = Interval(start, start + 3 * shift, other_closed)
interval2 = Interval(start + shift, start + 2 * shift, closed)

# nested intervals should always overlap
assert interval1.overlaps(interval2)
