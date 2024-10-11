# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# Result should be cast back to DatetimeArray
box = box_with_array

dti = pd.date_range("2016-01-01", periods=3, tz=tz_naive_fixture)
dti = dti._with_freq(None)
tdi = dti - dti

obj = tm.box_expected(tdi, box)
other = tm.box_expected(dti, box)

with tm.assert_produces_warning(PerformanceWarning):
    result = obj + other.astype(object)
tm.assert_equal(result, other.astype(object))
