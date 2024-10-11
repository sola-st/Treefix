# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH 26258
tz = tz_aware_fixture
date = date_range(start="01 Jan 2014", end="01 Jan 2017", freq="AS", tz=tz)
date = tm.box_expected(date, box_with_array, False)
mth = getattr(date, op)
result = mth(offset)

expected = DatetimeIndex(exp, tz=tz)
expected = tm.box_expected(expected, box_with_array, False)
tm.assert_equal(result, expected)
