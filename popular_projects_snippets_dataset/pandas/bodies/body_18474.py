# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#17558
tz = tz_naive_fixture
dti = DatetimeIndex([Timestamp("2017-01-01", tz=tz)] * 10)
tdi = pd.timedelta_range("0 days", periods=10)
expected = date_range("2017-01-01", periods=10, tz=tz, freq="-1D")
expected = expected._with_freq(None)

# sub with TimedeltaIndex
result = dti - tdi
tm.assert_index_equal(result, expected)

msg = "cannot subtract .*TimedeltaArray"
with pytest.raises(TypeError, match=msg):
    tdi - dti

# sub with timedelta64 array
result = dti - tdi.values
tm.assert_index_equal(result, expected)

msg = "cannot subtract a datelike from a TimedeltaArray"
with pytest.raises(TypeError, match=msg):
    tdi.values - dti
