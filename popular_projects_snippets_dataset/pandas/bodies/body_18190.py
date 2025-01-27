# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx

expected = Index([np.nan, np.nan, np.nan, np.nan, np.nan], dtype=np.float64)
result = idx % zero
tm.assert_index_equal(result, expected)
ser_compat = Series(idx).astype("i8") % np.array(zero).astype("i8")
tm.assert_series_equal(ser_compat, Series(result))
