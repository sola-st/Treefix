# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
tz = tz_naive_fixture

dti = date_range("2017-01-01", periods=2, tz=tz)
dtarr = tm.box_expected(dti, box_with_array)
other = other_box([pd.offsets.MonthEnd(), Timedelta(days=4)])
xbox = get_upcast_box(dtarr, other)

expected = DatetimeIndex(["2017-01-31", "2017-01-06"], tz=tz_naive_fixture)
expected = tm.box_expected(expected, xbox).astype(object)

with tm.assert_produces_warning(PerformanceWarning):
    result = dtarr + other
tm.assert_equal(result, expected)

expected = DatetimeIndex(["2016-12-31", "2016-12-29"], tz=tz_naive_fixture)
expected = tm.box_expected(expected, xbox).astype(object)

with tm.assert_produces_warning(PerformanceWarning):
    result = dtarr - other
tm.assert_equal(result, expected)
