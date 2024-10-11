# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# with datetimes/timedelta and tdi/dti
tdi = TimedeltaIndex(["1 days", NaT, "2 days"], name="foo")
dti = pd.date_range("20130101", periods=3, name="bar")
td = Timedelta("1 days")
dt = Timestamp("20130101")

result = tdi + dt
expected = DatetimeIndex(["20130102", NaT, "20130103"], name="foo")
tm.assert_index_equal(result, expected)

result = dt + tdi
expected = DatetimeIndex(["20130102", NaT, "20130103"], name="foo")
tm.assert_index_equal(result, expected)

result = td + tdi
expected = TimedeltaIndex(["2 days", NaT, "3 days"], name="foo")
tm.assert_index_equal(result, expected)

result = tdi + td
expected = TimedeltaIndex(["2 days", NaT, "3 days"], name="foo")
tm.assert_index_equal(result, expected)

# unequal length
msg = "cannot add indices of unequal length"
with pytest.raises(ValueError, match=msg):
    tdi + dti[0:1]
with pytest.raises(ValueError, match=msg):
    tdi[0:1] + dti

# random indexes
msg = "Addition/subtraction of integers and integer-arrays"
with pytest.raises(TypeError, match=msg):
    tdi + NumericIndex([1, 2, 3], dtype=np.int64)

# this is a union!
# pytest.raises(TypeError, lambda : Index([1,2,3]) + tdi)

result = tdi + dti  # name will be reset
expected = DatetimeIndex(["20130102", NaT, "20130105"])
tm.assert_index_equal(result, expected)

result = dti + tdi  # name will be reset
expected = DatetimeIndex(["20130102", NaT, "20130105"])
tm.assert_index_equal(result, expected)

result = dt + td
expected = Timestamp("20130102")
assert result == expected

result = td + dt
expected = Timestamp("20130102")
assert result == expected
