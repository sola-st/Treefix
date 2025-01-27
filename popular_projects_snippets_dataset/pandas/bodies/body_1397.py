# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH3216
df = DataFrame([{"a": 1}, {"a": 3, "b": 2}])
df["c"] = np.nan
assert df["c"].dtype == np.float64

df.loc[0, "c"] = "foo"
expected = DataFrame(
    [{"a": 1, "b": np.nan, "c": "foo"}, {"a": 3, "b": 2, "c": np.nan}]
)
tm.assert_frame_equal(df, expected)
