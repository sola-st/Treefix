# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#17558
tz = tz_naive_fixture
dti = DatetimeIndex([Timestamp("2017-01-01", tz=tz)] * 10)
tdi = pd.timedelta_range("0 days", periods=10)
expected = date_range("2017-01-01", periods=10, tz=tz)
expected = expected._with_freq(None)

# iadd with TimedeltaIndex
result = DatetimeIndex([Timestamp("2017-01-01", tz=tz)] * 10)
result += tdi
tm.assert_index_equal(result, expected)

result = pd.timedelta_range("0 days", periods=10)
result += dti
tm.assert_index_equal(result, expected)

# iadd with timedelta64 array
result = DatetimeIndex([Timestamp("2017-01-01", tz=tz)] * 10)
result += tdi.values
tm.assert_index_equal(result, expected)

result = pd.timedelta_range("0 days", periods=10)
result += dti
tm.assert_index_equal(result, expected)
