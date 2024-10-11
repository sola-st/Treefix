# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH 34474
start, end = "2000-10-01 23:30:00+0500", "2000-12-02 00:30:00+0500"
rng = date_range(start, end, freq="7min").as_unit(unit)
random_values = np.random.randn(len(rng))
ts_1 = Series(random_values, index=rng)

result_1 = ts_1.resample("D", origin="epoch").mean()
result_2 = ts_1.resample("24H", origin="epoch").mean()
tm.assert_series_equal(result_1, result_2)

# check that we have the same behavior with epoch even if we are not timezone aware
ts_no_tz = ts_1.tz_localize(None)
result_3 = ts_no_tz.resample("D", origin="epoch").mean()
result_4 = ts_no_tz.resample("24H", origin="epoch").mean()
tm.assert_series_equal(result_1, result_3.tz_localize(rng.tz), check_freq=False)
tm.assert_series_equal(result_1, result_4.tz_localize(rng.tz), check_freq=False)

# check that we have the similar results with two different timezones (+2H and +5H)
start, end = "2000-10-01 23:30:00+0200", "2000-12-02 00:30:00+0200"
rng = date_range(start, end, freq="7min").as_unit(unit)
ts_2 = Series(random_values, index=rng)
result_5 = ts_2.resample("D", origin="epoch").mean()
result_6 = ts_2.resample("24H", origin="epoch").mean()
tm.assert_series_equal(result_1.tz_localize(None), result_5.tz_localize(None))
tm.assert_series_equal(result_1.tz_localize(None), result_6.tz_localize(None))
