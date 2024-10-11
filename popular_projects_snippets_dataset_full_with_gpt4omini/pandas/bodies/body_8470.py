# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_unique.py
arr = [
    Timestamp("2013-06-09 02:42:28") + timedelta(seconds=t) for t in range(20)
] + [NaT]
idx = DatetimeIndex(arr * 3)
tm.assert_index_equal(idx.unique(), DatetimeIndex(arr))
assert idx.nunique() == 20
assert idx.nunique(dropna=False) == 21
