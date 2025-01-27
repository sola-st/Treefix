# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH 8209
s = Series([], dtype=object)
s.loc["B"] = timedelta(1)
tm.assert_series_equal(s, Series(Timedelta("1 days"), index=["B"]))

s = s.reindex(s.index.insert(0, "A"))
tm.assert_series_equal(s, Series([np.nan, Timedelta("1 days")], index=["A", "B"]))

s.loc["A"] = timedelta(1)
expected = Series(Timedelta("1 days"), index=["A", "B"])
tm.assert_series_equal(s, expected)
