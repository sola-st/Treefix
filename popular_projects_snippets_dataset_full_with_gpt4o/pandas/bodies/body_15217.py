# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_delitem.py
# Index(dtype=object)
s = Series(1, index=["a"])
del s["a"]
tm.assert_series_equal(
    s, Series(dtype="int64", index=Index([], dtype="object"))
)
s["a"] = 1
tm.assert_series_equal(s, Series(1, index=["a"]))
del s["a"]
tm.assert_series_equal(
    s, Series(dtype="int64", index=Index([], dtype="object"))
)
