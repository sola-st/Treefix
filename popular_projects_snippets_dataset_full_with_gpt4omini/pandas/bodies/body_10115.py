# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
# GH#46560
ser = Series([1, 2, 3], dtype=dtype)
arg = (ser,) if use_arg else ()
ewm = ser.ewm(span=2, min_periods=1)
op = getattr(ewm, kernel)
if numeric_only and dtype is object:
    msg = f"ExponentialMovingWindow.{kernel} does not implement numeric_only"
    with pytest.raises(NotImplementedError, match=msg):
        op(*arg, numeric_only=numeric_only)
else:
    result = op(*arg, numeric_only=numeric_only)

    ser2 = ser.astype(float)
    arg2 = (ser2,) if use_arg else ()
    ewm2 = ser2.ewm(span=2, min_periods=1)
    op2 = getattr(ewm2, kernel)
    expected = op2(*arg2, numeric_only=numeric_only)
    tm.assert_series_equal(result, expected)
