# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#17607
idx = RangeIndex(start, stop, step)
expected = idx._values.max()
result = idx.max()
assert result == expected

# skipna should be irrelevant since RangeIndex should never have NAs
result2 = idx.max(skipna=False)
assert result2 == expected

expected = idx._values.min()
result = idx.min()
assert result == expected

# skipna should be irrelevant since RangeIndex should never have NAs
result2 = idx.min(skipna=False)
assert result2 == expected

# empty
idx = RangeIndex(start, stop, -step)
assert isna(idx.max())
assert isna(idx.min())
