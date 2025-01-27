# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_level_values.py
# GH#49054
idx = pd.DatetimeIndex(date_range("20200101", periods=3, freq="BM"))
expected = idx.copy(deep=True)
idx2 = Index([1, 2, 3])
midx = MultiIndex(levels=[idx, idx2], codes=[[0, 1, 2], [0, 1, 2]])
midx.values
assert idx.freq is not None
tm.assert_index_equal(idx, expected)
