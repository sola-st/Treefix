# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py

df = DataFrame(0, index=range(3), columns=["tt1", "tt2"], dtype=np.int_)
df.loc[1, ["tt1", "tt2"]] = [1, 2]

result = df.loc[df.index[1], ["tt1", "tt2"]]
expected = Series([1, 2], df.columns, dtype=np.int_, name=1)
tm.assert_series_equal(result, expected)

df["tt1"] = df["tt2"] = "0"
df.loc[df.index[1], ["tt1", "tt2"]] = ["1", "2"]
result = df.loc[df.index[1], ["tt1", "tt2"]]
expected = Series(["1", "2"], df.columns, name=1)
tm.assert_series_equal(result, expected)
