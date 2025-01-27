# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
box = box_with_array

tdi = TimedeltaIndex(["1 Day"] * 10)
expected = timedelta_range("1 days", "10 days")._with_freq(None)

tdi = tm.box_expected(tdi, box)
xbox = get_upcast_box(tdi, other)

expected = tm.box_expected(expected, xbox)

result = other * tdi
tm.assert_equal(result, expected)
commute = tdi * other
tm.assert_equal(commute, expected)
