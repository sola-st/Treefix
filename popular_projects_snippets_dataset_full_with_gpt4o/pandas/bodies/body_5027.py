# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
start, shift = start_shift
interval = Interval(start, start + shift, closed)
assert interval.overlaps(interval)
