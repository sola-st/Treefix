# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
# GH#48636
midx = MultiIndex.from_arrays([[]], names=["A"])
result = midx.set_levels(pd.DatetimeIndex([]), level=0)
expected = MultiIndex.from_arrays([pd.DatetimeIndex([])], names=["A"])
tm.assert_index_equal(result, expected)
