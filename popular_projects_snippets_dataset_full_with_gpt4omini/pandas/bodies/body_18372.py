# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
tdi = timedelta_range("1 Day", "9 days")
tdarr = tm.box_expected(tdi, box_with_array)

expected = TimedeltaIndex(["1 Day", "2 Days", "0 Days"] * 3)
expected = tm.box_expected(expected, box_with_array)

result = tdarr % three_days
tm.assert_equal(result, expected)

warn = None
if box_with_array is DataFrame and isinstance(three_days, pd.DateOffset):
    warn = PerformanceWarning
    # TODO: making expected be object here a result of DataFrame.__divmod__
    #  being defined in a naive way that does not dispatch to the underlying
    #  array's __divmod__
    expected = expected.astype(object)

with tm.assert_produces_warning(warn):
    result = divmod(tdarr, three_days)

tm.assert_equal(result[1], expected)
tm.assert_equal(result[0], tdarr // three_days)
