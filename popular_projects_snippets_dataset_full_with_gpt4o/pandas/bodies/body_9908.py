# Extracted from ./data/repos/pandas/pandas/tests/window/test_dtypes.py
# GH 43016
ser = Series([0, 1, NA], dtype=any_signed_int_ea_dtype)
result = ser.rolling(2, step=step).mean()
expected = Series([np.nan, 0.5, np.nan])[::step]
tm.assert_series_equal(result, expected)
