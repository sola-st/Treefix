# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH#17157
# Check that the time part of the Period is adjusted by end_time
# when using the dt accessor on a Series
input_vals = PeriodArray._from_sequence(np.asarray(input_vals))

ser = Series(input_vals)
result = ser.dt.end_time
expected = ser.apply(lambda x: x.end_time)
tm.assert_series_equal(result, expected)
