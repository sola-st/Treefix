# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
s = Series(np.arange(10), dtype="int64")
s2 = s[::2]

reindexed = s2.reindex(s.index, method="pad")
reindexed2 = s2.reindex(s.index, method="ffill")
tm.assert_series_equal(reindexed, reindexed2)

expected = Series([0, 0, 2, 2, 4, 4, 6, 6, 8, 8])
tm.assert_series_equal(reindexed, expected)

# GH4604
s = Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
new_index = ["a", "g", "c", "f"]
expected = Series([1, 1, 3, 3], index=new_index)

# this changes dtype because the ffill happens after
result = s.reindex(new_index).ffill()
tm.assert_series_equal(result, expected.astype("float64"))

result = s.reindex(new_index).ffill(downcast="infer")
tm.assert_series_equal(result, expected)

expected = Series([1, 5, 3, 5], index=new_index)
result = s.reindex(new_index, method="ffill")
tm.assert_series_equal(result, expected)

# inference of new dtype
s = Series([True, False, False, True], index=list("abcd"))
new_index = "agc"
result = s.reindex(list(new_index)).ffill()
expected = Series([True, True, False], index=list(new_index))
tm.assert_series_equal(result, expected)

# GH4618 shifted series downcasting
s = Series(False, index=range(0, 5))
result = s.shift(1).fillna(method="bfill")
expected = Series(False, index=range(0, 5))
tm.assert_series_equal(result, expected)
