# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# https://github.com/pandas-dev/pandas/issues/35471
ser = Series(data, dtype=dtype)
if errors == "ignore":
    expected = ser
    result = ser.astype(float, errors="ignore")
    tm.assert_series_equal(result, expected)
else:
    msg = "(Cannot cast)|(could not convert)"
    with pytest.raises((ValueError, TypeError), match=msg):
        ser.astype(float, errors=errors)
