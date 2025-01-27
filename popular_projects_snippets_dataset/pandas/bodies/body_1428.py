# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# Check that .iloc returns correct dtypes GH9983
df = DataFrame({"a": [1, 2, 3], "b": ["b", "b2", "b3"]})
df2 = df.iloc[[], :]

assert df2.loc[:, "a"].dtype == np.int64
tm.assert_series_equal(df2.loc[:, "a"], df2.iloc[:, 0])
