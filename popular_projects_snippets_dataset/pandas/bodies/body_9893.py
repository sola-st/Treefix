# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH#46560
kernel = arithmetic_win_operators
ser = Series([1], dtype=dtype)
rolling = ser.rolling(2, min_periods=1)
op = getattr(rolling, kernel)
if numeric_only and dtype is object:
    msg = f"Rolling.{kernel} does not implement numeric_only"
    with pytest.raises(NotImplementedError, match=msg):
        op(numeric_only=numeric_only)
else:
    result = op(numeric_only=numeric_only)
    expected = ser.agg([kernel]).reset_index(drop=True).astype(float)
    tm.assert_series_equal(result, expected)
