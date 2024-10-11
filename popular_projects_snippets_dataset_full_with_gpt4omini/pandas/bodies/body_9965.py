# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH#46560
ser = Series([1, 2, 3], dtype=dtype)
arg = (ser,) if use_arg else ()
expanding = ser.expanding()
op = getattr(expanding, kernel)
if numeric_only and dtype is object:
    msg = f"Expanding.{kernel} does not implement numeric_only"
    with pytest.raises(NotImplementedError, match=msg):
        op(*arg, numeric_only=numeric_only)
else:
    result = op(*arg, numeric_only=numeric_only)

    ser2 = ser.astype(float)
    arg2 = (ser2,) if use_arg else ()
    expanding2 = ser2.expanding()
    op2 = getattr(expanding2, kernel)
    expected = op2(*arg2, numeric_only=numeric_only)
    tm.assert_series_equal(result, expected)
