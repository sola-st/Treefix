# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# https://github.com/pandas-dev/pandas/pull/32490
ser = pd.Series([1, 2], dtype=dtype)
orig = ser.copy()

err = False
if (dtype == "datetime64[ns]") ^ (other == "datetime64[ns]"):
    # deprecated in favor of tz_localize
    err = True

if err:
    if dtype == "datetime64[ns]":
        msg = "Use obj.tz_localize instead or series.dt.tz_localize instead"
    else:
        msg = "from timezone-aware dtype to timezone-naive dtype"
    with pytest.raises(TypeError, match=msg):
        ser.astype(other)
else:
    t = ser.astype(other)
    t[:] = pd.NaT
    tm.assert_series_equal(ser, orig)
