# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# https://github.com/pandas-dev/pandas/issues/31449
index = MultiIndex.from_tuples(
    [("a", "c"), ("b", "x"), ("a", "d")], names=["l1", "l2"]
)
df = DataFrame(data=[0, 1, 2], index=index, columns=["e"])
df.loc["a", "e"] = np.arange(99, 101, dtype="int64")
expected = DataFrame({"e": [99, 1, 100]}, index=index)
tm.assert_frame_equal(df, expected)
