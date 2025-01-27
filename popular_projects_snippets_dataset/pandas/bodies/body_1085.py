# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
frame = multiindex_dataframe_random_data
dft = frame.T
s = dft["foo", "two"]
dft["foo", "two"] = s > s.median()
tm.assert_series_equal(dft["foo", "two"], s > s.median())
# assert isinstance(dft._data.blocks[1].items, MultiIndex)

reindexed = dft.reindex(columns=[("foo", "two")])
tm.assert_series_equal(reindexed["foo", "two"], s > s.median())
