# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#17558
tz = tz_naive_fixture
dti = DatetimeIndex([Timestamp("2017-01-01", tz=tz)] * 10)
tdi = pd.timedelta_range("0 days", periods=10)
expected = date_range("2017-01-01", periods=10, tz=tz)
expected = expected._with_freq(None)

# add with TimedeltaIndex
result = dti + tdi
tm.assert_index_equal(result, expected)

result = tdi + dti
tm.assert_index_equal(result, expected)

# add with timedelta64 array
result = dti + tdi.values
tm.assert_index_equal(result, expected)

result = tdi.values + dti
tm.assert_index_equal(result, expected)
