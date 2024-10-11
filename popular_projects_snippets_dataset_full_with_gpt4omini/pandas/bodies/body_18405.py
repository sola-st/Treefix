# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
interval_array = IntervalArray.from_arrays(range(4), range(1, 5))
other = other_constructor([Interval(0, 1)] * length)
with pytest.raises(ValueError, match="Lengths must match to compare"):
    op(interval_array, other)
