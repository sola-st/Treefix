# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_sorted.py
index_columns = list("abc")
df = DataFrame(
    [[0, 1, 0, "x"], [0, 0, 1, "y"]], columns=index_columns + ["data"]
)
df = df.set_index(index_columns)
query_index = df.index[:1]
rs = df.loc[query_index, "data"]

xp_idx = MultiIndex.from_tuples([(0, 1, 0)], names=["a", "b", "c"])
xp = Series(["x"], index=xp_idx, name="data")
tm.assert_series_equal(rs, xp)
