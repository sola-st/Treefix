# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#13905
tz = tz_naive_fixture
index = DatetimeIndex(
    ["2016-06-28 05:30", "2016-06-28 05:31"], tz=tz, name=names[0]
)
ser = Series([Timedelta(seconds=5)] * 2, index=index, name=names[1])
expected = Series(index + Timedelta(seconds=5), index=index, name=names[2])

# passing name arg isn't enough when names[2] is None
expected.name = names[2]
assert expected.dtype == index.dtype
result = ser + index
tm.assert_series_equal(result, expected)
result2 = index + ser
tm.assert_series_equal(result2, expected)

expected = index + Timedelta(seconds=5)
result3 = ser.values + index
tm.assert_index_equal(result3, expected)
result4 = index + ser.values
tm.assert_index_equal(result4, expected)
