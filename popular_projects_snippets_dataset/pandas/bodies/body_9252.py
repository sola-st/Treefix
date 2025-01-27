# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# GH#23705
cat = Categorical(IntervalIndex.from_breaks(range(3)))
result = item in cat
assert result is expected
