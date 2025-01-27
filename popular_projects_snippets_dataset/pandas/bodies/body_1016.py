# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py
# GH 12697
freq = ["a", "b", "c", "d"]
idx = MultiIndex.from_product([freq, range(500)])
df = DataFrame(list(range(2000)), index=idx, columns=["Test"])
df_slice = df.loc[pd.IndexSlice[:, 30:70], :]
result = df_slice.loc["a"]
expected = DataFrame(list(range(30, 71)), columns=["Test"], index=range(30, 71))
tm.assert_frame_equal(result, expected)
result = df_slice.loc["d"]
expected = DataFrame(
    list(range(1530, 1571)), columns=["Test"], index=range(30, 71)
)
tm.assert_frame_equal(result, expected)
