# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
df = multiindex_dataframe_random_data
result = df.xs(("bar", "two"))
expected = df.loc[("bar", "two")]
tm.assert_series_equal(result, expected)
