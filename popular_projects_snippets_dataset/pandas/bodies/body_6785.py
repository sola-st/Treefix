# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH#27571 dir(interval_index) should not raise
index = IntervalIndex.from_arrays([0, 1], [1, 2])
result = dir(index)
assert "str" not in result
