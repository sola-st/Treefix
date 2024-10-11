# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
tdi = timedelta_range("1 Day", "9 days")
tdarr = tm.box_expected(tdi, box_with_array)

expected = ["0 Days", "1 Day", "0 Days"] + ["3 Days"] * 6
expected = TimedeltaIndex(expected)
expected = tm.box_expected(expected, box_with_array)

result = three_days % tdarr
tm.assert_equal(result, expected)

result = divmod(three_days, tdarr)
tm.assert_equal(result[1], expected)
tm.assert_equal(result[0], three_days // tdarr)
