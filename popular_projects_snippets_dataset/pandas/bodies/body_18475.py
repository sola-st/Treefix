# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#17558
tz = tz_naive_fixture
dti = DatetimeIndex([Timestamp("2017-01-01", tz=tz)] * 10)
tdi = pd.timedelta_range("0 days", periods=10)
expected = date_range("2017-01-01", periods=10, tz=tz, freq="-1D")
expected = expected._with_freq(None)

# isub with TimedeltaIndex
result = DatetimeIndex([Timestamp("2017-01-01", tz=tz)] * 10)
result -= tdi
tm.assert_index_equal(result, expected)

# DTA.__isub__ GH#43904
dta = dti._data.copy()
dta -= tdi
tm.assert_datetime_array_equal(dta, expected._data)

out = dti._data.copy()
np.subtract(out, tdi, out=out)
tm.assert_datetime_array_equal(out, expected._data)

msg = "cannot subtract a datelike from a TimedeltaArray"
with pytest.raises(TypeError, match=msg):
    tdi -= dti

# isub with timedelta64 array
result = DatetimeIndex([Timestamp("2017-01-01", tz=tz)] * 10)
result -= tdi.values
tm.assert_index_equal(result, expected)

with pytest.raises(TypeError, match=msg):
    tdi.values -= dti

with pytest.raises(TypeError, match=msg):
    tdi._values -= dti
