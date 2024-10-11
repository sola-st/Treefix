# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_downcast.py
# see gh-16875: coercing of booleans.
ser = Series([True, True, False])
result = maybe_downcast_to_dtype(ser, np.dtype(np.float64))

expected = ser
tm.assert_series_equal(result, expected)
