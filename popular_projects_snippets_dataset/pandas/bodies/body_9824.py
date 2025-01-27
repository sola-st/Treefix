# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# see gh-21704
ser = Series(
    data=np.arange(10).astype(input_dtype),
    index=date_range("2000", periods=10),
)

result = getattr(ser.rolling("3D", closed=closed), func)()
expected = Series(expected, index=ser.index)
tm.assert_series_equal(result, expected)
