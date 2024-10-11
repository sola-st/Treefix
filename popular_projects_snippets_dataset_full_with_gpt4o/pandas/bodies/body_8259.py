# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
# GH#33703
tz = tz_aware_fixture
dti = date_range("2019-11-04", periods=3, freq="-1D", name=9, tz=tz)

value = "2019-11-05"
result = dti.insert(0, value)

ts = Timestamp(value).tz_localize(tz)
expected = DatetimeIndex([ts] + list(dti), dtype=dti.dtype, name=9)
tm.assert_index_equal(result, expected)
