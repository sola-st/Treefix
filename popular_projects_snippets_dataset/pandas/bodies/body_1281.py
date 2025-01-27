# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

df = DataFrame(np.random.randn(10, 4))
ser = df.iloc[:, 0].sort_values()

tm.assert_series_equal(ser, df.iloc[:, 0].sort_values())
tm.assert_series_equal(ser, df[0].sort_values())
