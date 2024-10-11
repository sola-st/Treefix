# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# tznaive
ser = Series(date_range("20130101", periods=5, freq="D"), name="xxx")
results = get_dir(ser)
tm.assert_almost_equal(results, sorted(set(ok_for_dt + ok_for_dt_methods)))

# tzaware
ser = Series(date_range("2015-01-01", "2016-01-01", freq="T"), name="xxx")
ser = ser.dt.tz_localize("UTC").dt.tz_convert("America/Chicago")
results = get_dir(ser)
tm.assert_almost_equal(results, sorted(set(ok_for_dt + ok_for_dt_methods)))

# Period
ser = Series(
    period_range("20130101", periods=5, freq="D", name="xxx").astype(object)
)
results = get_dir(ser)
tm.assert_almost_equal(
    results, sorted(set(ok_for_period + ok_for_period_methods))
)
