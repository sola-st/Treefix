# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# https://github.com/pandas-dev/pandas/pull/24866
ser = Series([1, 2], dtype="int64")
# Don't have PandasDtype in the public API, so we use `.array.dtype`,
# which is a PandasDtype.
result = ser.astype(ser.array.dtype)
tm.assert_series_equal(result, ser)
