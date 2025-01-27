# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py

# GH29519
# test single level indexing on single index column data frame
df = DataFrame(np.arange(9).reshape(3, 3), columns=["a", "b", "c"])
result = df.loc(axis=1)["a"]
expected = Series(np.array([0, 3, 6]), name="a")
tm.assert_series_equal(result, expected)
