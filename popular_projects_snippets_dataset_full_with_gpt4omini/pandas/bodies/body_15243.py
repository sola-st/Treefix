# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_xs.py
df = multiindex_dataframe_random_data
ser = df["A"]
expected = ser[:, "two"]
result = df.xs("two", level=1)["A"]
tm.assert_series_equal(result, expected)
