# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_unique.py
# NaT, note this is excluded
arr = [1370745748 + t for t in range(20)] + [NaT.value]
idx = DatetimeIndex(arr * 3)
tm.assert_index_equal(idx.unique(), DatetimeIndex(arr))
assert idx.nunique() == 20
assert idx.nunique(dropna=False) == 21
