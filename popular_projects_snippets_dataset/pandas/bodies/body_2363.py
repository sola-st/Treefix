# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
df = multiindex_dataframe_random_data
result = df.xs(("bar", "two")).values
expected = df.values[4]
tm.assert_almost_equal(result, expected)
