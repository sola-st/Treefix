# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py
ser = Series(values, dtype=dtype)
result = ser.quantile([0.5])
expected = Series(np.asarray(ser)).quantile([0.5]).astype("Sparse[float]")
tm.assert_series_equal(result, expected)
