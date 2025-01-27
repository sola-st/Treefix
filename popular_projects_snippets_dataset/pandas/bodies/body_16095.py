# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 23324 round near "spring forward" DST
ser = Series([pd.Timestamp(ts_str, tz="America/Chicago")])
result = getattr(ser.dt, method)(freq, nonexistent="shift_forward")
expected = Series([pd.Timestamp("2018-03-11 03:00:00", tz="America/Chicago")])
tm.assert_series_equal(result, expected)

result = getattr(ser.dt, method)(freq, nonexistent="NaT")
expected = Series([pd.NaT]).dt.tz_localize(result.dt.tz)
tm.assert_series_equal(result, expected)

with pytest.raises(pytz.NonExistentTimeError, match="2018-03-11 02:00:00"):
    getattr(ser.dt, method)(freq, nonexistent="raise")
