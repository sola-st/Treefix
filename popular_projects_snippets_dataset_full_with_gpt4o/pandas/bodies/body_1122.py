# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 671
df = DataFrame(
    {
        "a": np.arange(10),
        "b": np.arange(10),
        "c": np.random.randn(10),
        "d": np.random.randn(10),
    }
).set_index(["a", "b"])
expected = df.loc[0, 0]
result = df.loc[(0, 0), :]
tm.assert_series_equal(result, expected)
